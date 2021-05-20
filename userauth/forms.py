from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelChoiceField
from stelaapp.models import Profile
from stelaapp.models import University
from django.forms.widgets import DateInput

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
        'DoB': ('Date of birth'),
        'university':('University')
        }
        widgets = {
            'DoB': DateInput(attrs={'type': 'date'}), 
        }
        fields = ('email', 'first_name', 'last_name','studentIdNumber','university', 'faculty','isCandidate','DoB')
        
        