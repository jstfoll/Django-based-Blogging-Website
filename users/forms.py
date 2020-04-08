from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", 'last_name','username','email','password1','password2']

    def clean_email(self):
                email = self.cleaned_data.get('email')
                if email:
                    if User.objects.filter(email=email).exists():
                        raise forms.ValidationError('Your email is not unique.')
                return email