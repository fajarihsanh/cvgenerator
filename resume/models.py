from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='cv_photos/', blank=True, null=True, help_text='Upload foto profil Anda')
    
    # Contact Information
    phone = models.CharField(max_length=20, blank=True, null=True, help_text='Nomor telepon')
    address = models.TextField(blank=True, null=True, help_text='Alamat lengkap')
    city = models.CharField(max_length=100, blank=True, null=True, help_text='Kota')
    country = models.CharField(max_length=100, blank=True, null=True, help_text='Negara')
    
    # Social Media & Professional Links
    github = models.URLField(blank=True, null=True, help_text='Link GitHub')
    linkedin = models.URLField(blank=True, null=True, help_text='Link LinkedIn')
    twitter = models.URLField(blank=True, null=True, help_text='Link Twitter/X')
    instagram = models.URLField(blank=True, null=True, help_text='Link Instagram')
    website = models.URLField(blank=True, null=True, help_text='Website pribadi')
    portfolio = models.URLField(blank=True, null=True, help_text='Link portfolio')
    
    # CV Content
    summary = RichTextField()
    experience = RichTextField()
    education = RichTextField()
    skills = RichTextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.job_title}"
    
    def get_contact_info(self):
        """Return all contact information as a dictionary"""
        return {
            'email': self.user.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'country': self.country,
        }
    
    def get_social_links(self):
        """Return all social media links as a dictionary"""
        return {
            'github': self.github,
            'linkedin': self.linkedin,
            'twitter': self.twitter,
            'instagram': self.instagram,
            'website': self.website,
            'portfolio': self.portfolio,
        }
