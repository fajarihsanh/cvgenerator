from django.contrib import admin
from .models import CV

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job_title', 'user', 'phone', 'city', 'country', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'city', 'country']
    search_fields = ['full_name', 'job_title', 'user__username', 'user__email', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informasi Pribadi', {
            'fields': ('user', 'full_name', 'job_title', 'profile_photo')
        }),
        ('Informasi Kontak', {
            'fields': ('phone', 'address', 'city', 'country'),
            'classes': ('collapse',)
        }),
        ('Media Sosial & Profesional', {
            'fields': ('github', 'linkedin', 'twitter', 'instagram', 'website', 'portfolio'),
            'classes': ('collapse',)
        }),
        ('Konten CV', {
            'fields': ('summary', 'experience', 'education', 'skills')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
