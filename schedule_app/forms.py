from django.forms import ModelForm
from .models import Planner
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#create class for project form
class PlannerForm(ModelForm):
    class Meta:
        model = Planner
        fields =('name', 'date', 'description')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
        