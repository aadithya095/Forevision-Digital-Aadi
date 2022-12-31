from django.urls import path
from .views import SingleReleaseFormView, DashboardView

app_name = 'client'

urlpatterns = [
        path('single-form/', SingleReleaseFormView.as_view(), name='single_form'),
        path('dashboard/', DashboardView.as_view(), name='dashboard'),
        ]
