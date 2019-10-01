"""
Definition of urls for serviceway.
"""

from datetime import datetime
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from app import forms, views

urlpatterns = [
    path('', include(('app.urls', "app"), "appurls")),
    path('favicon\.ico', RedirectView.as_view(url='/static/app/misc/favicon.ico', permanent=True)),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('seed/', views.seed, name='seed'),
    path('login/', 
        LoginView.as_view
        (
            template_name='app/login.html', 
            authentication_form=forms.BootstrapAuthenticationForm,
            extra_context =
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
         ),
        name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls)
]
