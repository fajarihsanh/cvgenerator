from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            'full_name', 'job_title', 'profile_photo',
            'phone', 'address', 'city', 'country',
            'github', 'linkedin', 'twitter', 'instagram', 'website', 'portfolio',
            'summary', 'experience', 'education', 'skills'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama lengkap'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan jabatan/posisi'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            
            # Contact fields
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+62 812-3456-7890'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Masukkan alamat lengkap'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jakarta'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indonesia'}),
            
            # Social media fields
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/username'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/username'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/username'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://yourwebsite.com'}),
            'portfolio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://portfolio.com'}),
        } 