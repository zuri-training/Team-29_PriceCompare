from .models import  ProductComment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('author', 'body')
