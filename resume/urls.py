from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/', views.edit_cv, name='edit_cv'),
    path('print/', views.print_cv, name='print_cv'),
    path('delete/', views.delete_cv, name='delete_cv'),
    path('view/', views.view_cv, name='view_cv'),
    path('logout/', views.logout_view, name='logout'),
] 