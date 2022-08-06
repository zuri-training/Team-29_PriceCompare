from .models import  ProductComment
from django import forms

class CommentForm(forms.Model):
    class Meta:
        model = ProductComment
        fields = ('author', 'body')