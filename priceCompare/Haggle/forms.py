from django import forms


class FormName(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs={
        "class": "thro",
        "type" : "text",
        "placeholder": "Joh Doe"

    }))
    email = forms.CharField(widget = forms.TextInput(attrs={
        "class": "thro",
        "type" : "text",
        "placeholder": "enter your email"

    }))

    password = forms.CharField(widget = forms.TextInput(attrs={
        "class": "thro",
        "type" : "text",
        "placeholder": "**********"

    }))

