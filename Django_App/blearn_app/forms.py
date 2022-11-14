from django import forms
from .models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'blur_word', 'content', 'category']
        labels = {
            'title':'タイトル',
            'blur_word':'隠したい単語',
            'content':'説明文',
            'category':'カテゴリ',
        }
