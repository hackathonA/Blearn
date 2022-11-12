from django import forms
from .models import Content

widget_textarea = forms.Textarea(
    attrs={
        "class": "form-control"
    }
)

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'blur_word', 'content', 'category']
        widgets = {
            'content': widget_textarea
        }
