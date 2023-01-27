from django.urls import path
from .views import (
        DashboardView,
        LandingPage,
        LoginPage,
        RegisterPage,
        OrderFormPage,
        # PartyFormPage,
                    )

app_name = 'client'

urlpatterns = [
        path('', LandingPage.as_view(), name='landing'),
        path('login/', LoginPage.as_view(), name='user_login'),
        path('register/', RegisterPage.as_view(), name='user_register'),
        path('dashboard/', DashboardView.as_view(), name='dashboard'),

        # Urls for form based views
        path('order-form/', OrderFormPage.as_view(), name='order_form'),
        # path('party-form/', PartyFormPage.as_view(), name='party_form'),
        ]
