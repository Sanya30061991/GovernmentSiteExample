from django.forms import ModelForm, TextInput, Textarea, DateInput, Select
from django.contrib.auth.models import User
from .models import Citizen



class UserReg(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        widgets = {
            'first_name' : TextInput(attrs={
                'class':"input--style-1",
                'type':"text",
                'placeholder':"NAME",
                'name':"name"
            }),
            'last_name' : TextInput(attrs={
                'class':"input--style-1",
                'type':"text",
                'placeholder':"SURNAME",
                'name':"surname"
            }),
            'email' : TextInput(attrs={
                'class':"input--style-1",
                'type':"text",
                'placeholder':"EMAIL",
                'name':"email"
            }),
            'password' : TextInput(attrs={
                'class':"input--style-1",
                'type':"text",
                'placeholder':"PASSWORD",
                'name':"password"
            }),
        }

class CitReg(ModelForm):
    class Meta:
        model = Citizen
        fields = [
            'birth_day',
            'gender',
            ]
        widgets = {
            
            'birth_day' : DateInput(attrs={
                'class':"input--style-1 js-datepicker",
                'type':"text",
                'placeholder':"BIRTHDATE",
                'name':"birthday",
            }),
            'gender' : Select(attrs={
                'name':'gender',
            }, 
                choices=(
                    'Male',
                    'Female',
                    'Other'
                    )
                ),
            
        }
