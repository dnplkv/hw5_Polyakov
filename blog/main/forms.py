from django.forms import ModelForm, Textarea, TextInput

from .models import Post, Subscriber


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название поста",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Краткое описание",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержание",
            }),
        }


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email_to", "author_id"]
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email подписчика",
            }),
            "author_id": TextInput(attrs={
                "class": "form-control",
                "placeholder": "ID автора",
            }),
        }
