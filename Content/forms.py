from django.forms import ModelForm, TextInput, Textarea, DateInput, Select
from django.contrib.auth.models import User
from .models import Citizen

class CitReg(ModelForm):
    class Meta:
        model = Citizen
        fields = [
            'first_name',
            'last_name',
            'birth_day',
            'gender',
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
            'birth_day' : DateInput(attrs={
                'class':"input--style-1 js-datepicker",
                'type':"text",
                'placeholder':"BIRTHDATE",
                'name':"birthday",
            }),
            'gender' : Select(attrs={
                'disabled':"disabled",
                'selected':"selected",
                'name':'gender'
            }, 
                choices=(
                    'Male',
                    'Female',
                    'Other'
                    )
                ),
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
