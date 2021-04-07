from django import forms
from django.forms import ModelForm, Textarea, TextInput

from .models import Author, Post, Subscriber


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Post title--------------",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Brief description",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Content",
            }),
        }


class SubscriberForm(ModelForm):
    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('name'),
        empty_label="Enter Author",
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )

    class Meta:
        model = Subscriber
        fields = ["email_to", "author_id"]
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subscriber Email",
            }),
        }
