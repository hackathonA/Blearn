from django import forms
from .models import Content


class ContentForm(forms.ModelForm):
    category = forms.ChoiceField()
    class Meta:
        model = Content
        fields = ['title', 'blur_word', 'content', 'category']

    def __init__(self, categories=None, *args, **kwargs):
        self.base_fields["category"].choices = categories
        super().__init__(*args, **kwargs)
