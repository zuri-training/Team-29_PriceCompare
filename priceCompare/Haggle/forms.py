from .models import  ProductComment
from django import forms

class CommentForm(forms.Form):
    class Meta:
        model = ProductComment
        fields = ('author', 'body')
