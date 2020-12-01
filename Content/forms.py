from django.forms import ModelForm, TextInput, Textarea, DateInput, Select
from django.contrib.auth.models import User
from .models import Citizen

class UserLog(ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]
        widgets = {
            'email' : TextInput(attrs={
                'class':"input100",
                'type':"email",
                'name':"email"
            }),
            'password' : TextInput(attrs={
                'class':"input100",
                'type':"password",
                'name':"password"
            }),
        }

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
