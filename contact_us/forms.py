from django import forms
from .models import Contact_Us

class contact_us_form(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Please enter your name",
        "max_length": "Please enter a shorter name",
    })
    email = forms.EmailField(label="Your Email", error_messages={})
    contact_message = forms.CharField(label="Your Message", max_length=200, error_messages={}, widget=forms.Textarea)

class Contact_Us_Modelform(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = '__all__'
        #exclude = can be used to tell what wil not be included in the form.
        labels = {
            "user_name": "Your Name",
            "email": "Your Email",
        },
        error_messages = {
            "user_name":{
                "required":"Please enter your name",
            }
        }