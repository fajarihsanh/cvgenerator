from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.conf import settings
from django.db import transaction
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import os
from .models import CV
from .forms import CVForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    # Force refresh user from database
    from django.contrib.auth.models import User
    current_user = User.objects.get(id=request.user.id)
    
    # Clear any cached CV data
    if hasattr(request, '_cached_cv'):
        delattr(request, '_cached_cv')
    
    # Get or create CV for current user only with transaction
    with transaction.atomic():
        cv, created = CV.objects.get_or_create(user=current_user)
        
        # Force refresh CV from database
        cv.refresh_from_db()
        
        # Double-check security - verify ownership
        if cv.user.id != current_user.id:
            messages.error(request, 'Akses ditolak! Terjadi kesalahan keamanan.')
            # Clear session and redirect to login
            request.session.flush()
            logout(request)
            return redirect('login')
    
    context = {
        'cv': cv,
    }
    return render(request, 'resume/dashboard.html', context)

@login_required
def edit_cv(request):
    # Force refresh user from database
    from django.contrib.auth.models import User
    current_user = User.objects.get(id=request.user.id)
    
    # Get CV for current user only with transaction
    with transaction.atomic():
        try:
            cv = CV.objects.select_for_update().get(user=current_user)
        except CV.DoesNotExist:
            cv = CV.objects.create(user=current_user)
        
        # Security check
        if cv.user.id != current_user.id:
            messages.error(request, 'Akses ditolak! Anda tidak memiliki izin untuk mengedit CV ini.')
            return redirect('dashboard')
    
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV berhasil diperbarui!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan coba lagi.')
    else:
        form = CVForm(instance=cv)
    
    context = {
        'form': form,
        'cv': cv,
    }
    return render(request, 'resume/edit_cv.html', context)

@login_required
def print_cv(request):
    # Force refresh user from database
    from django.contrib.auth.models import User
    current_user = User.objects.get(id=request.user.id)
    
    # Get CV for current user only
    cv = get_object_or_404(CV, user=current_user)
    
    # Security check
    if cv.user.id != current_user.id:
        raise Http404("CV tidak ditemukan atau Anda tidak memiliki akses.")
    
    context = {'cv': cv}
    
    # Render template untuk PDF
    html_content = render_to_string('resume/print_cv.html', context)
    
    # Konfigurasi font
    font_config = FontConfiguration()
    
    # Generate PDF
    html = HTML(string=html_content, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf(font_config=font_config)
    
    # Buat response PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="CV_{cv.full_name.replace(" ", "_")}.pdf"'
    return response

@login_required
def delete_cv(request):
    # Force refresh user from database
    from django.contrib.auth.models import User
    current_user = User.objects.get(id=request.user.id)
    
    # Get CV for current user only
    cv = get_object_or_404(CV, user=current_user)
    
    # Security check
    if cv.user.id != current_user.id:
        messages.error(request, 'Akses ditolak! Anda tidak memiliki izin untuk menghapus CV ini.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        cv.delete()
        messages.success(request, 'CV berhasil dihapus!')
        return redirect('dashboard')
    
    context = {
        'cv': cv,
    }
    return render(request, 'resume/delete_cv.html', context)

@login_required
def view_cv(request):
    # Force refresh user from database
    from django.contrib.auth.models import User
    current_user = User.objects.get(id=request.user.id)
    
    # Get CV for current user only
    cv = get_object_or_404(CV, user=current_user)
    
    # Security check
    if cv.user.id != current_user.id:
        raise Http404("CV tidak ditemukan atau Anda tidak memiliki akses.")
    
    context = {
        'cv': cv,
    }
    return render(request, 'resume/view_cv.html', context)

def logout_view(request):
    # Clear all session data and cache
    request.session.flush()
    request.session.clear()
    
    # Clear any cached data
    if hasattr(request, '_cached_cv'):
        delattr(request, '_cached_cv')
    
    logout(request)
    messages.success(request, 'Anda berhasil logout.')
    return redirect('login')
