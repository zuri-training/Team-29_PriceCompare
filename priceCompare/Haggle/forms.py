from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'class':'form-input',
        })

        self.fields["email"].widget.attrs.update({
            'name':'usernmae',
            'id':'username',
            'class':'form-input',
        })
        self.fields["password1"].widget.attrs.update({
            'name':'usernmae',
            'id':'username',
            'class':'form-input',
        })
        self.fields["password2"].widget.attrs.update({
            'name':'usernmae',
            'id':'username',
            'class':'form-input',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']