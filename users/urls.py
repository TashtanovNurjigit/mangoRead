from django.urls import path

from .views import RegistrationAPIView, AuthorizationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', AuthorizationAPIView.as_view()),
]
