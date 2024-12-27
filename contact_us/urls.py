from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us),
    path('thank_you', views.thank_you),
]