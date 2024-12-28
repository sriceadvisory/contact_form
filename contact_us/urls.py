from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view()),
    path('thank_you',views.ThankYouView.as_view()),
    path("contact_list", views.ContactListView.as_view()),

]