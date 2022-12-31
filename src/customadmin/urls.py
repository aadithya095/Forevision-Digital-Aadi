from django.urls import path
from .views import admin_login, admin_dashboard

app_name = "customadmin"
urlpatterns = [
        path('', admin_login, name='login'),
        path('dashboard/', admin_dashboard, name='dashboard'),
        ]
