from django.urls import path
from . import views
# from .views import (
#         DashboardView,
#         LandingPage,
#         LoginPage,
#         RegisterPage,
#         OrderFormPage,
#         # PartyFormPage,
#                     )


urlpatterns = [
    path('', views.singleRelease, name='singleRelease'),
    # path('', LandingPage.as_view(), name='landing'),
    # path('login/', views.LoginPage.as_view(), name='user_login'),
    # path('register/', RegisterPage.as_view(), name='user_register'),
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # # Urls for form based views
    # path('order-form/', OrderFormPage.as_view(), name='order_form'),
    # # path('party-form/', PartyFormPage.as_view(), name='party_form'),
]
