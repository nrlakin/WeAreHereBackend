from django import forms
from django.contrib.auth.models import User
from wah_test.models import Occupant

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class OccupantForm(forms.ModelForm):
    class Meta:
        model = Occupant
        fields = ('room_id',)
