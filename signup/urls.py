from django.urls import path
from .views import SignUpView


urlpatterns = [
    path('registro/', SignUpView.as_view(), name='signup'),
]