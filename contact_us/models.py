from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_message = models.TextField()