from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from .models import Citizen

class CitReg(ModelForm):
    class Meta:
        model = Citizen
        fields = [
            'first_name',
            'email',
            'password',
            '',

            ]
        widgets = {
            'first_name' : TextInput(attrs = {
                'type':"text",
                'class':"form-control",
                'placeholder':"Name"
            }),
            'email' : TextInput(attrs = {
                'type':"email",
                'class':"form-control",
                'placeholder':"Email Address"
            }),
            'password' : TextInput(attrs = {
                'type':"password",
                'class':"form-control",
                'placeholder':"Password"
            }),
            'last_name' : TextInput(attrs = {
                'type':"password",
                'class':"form-control",
                'placeholder':"Confirm Password"
            })
        }
