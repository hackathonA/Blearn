from django import forms
from .models import Content


class ContentForm(forms.ModelForm):
    category = forms.ChoiceField()
    class Meta:
        model = Content
        fields = ['title', 'blur_word', 'content', 'category']
        labels = {
            'title':'タイトル',
            'blur_word':'隠したい単語',
            'content':'説明文',
            # 'category':'カテゴリ',
        }

    def __init__(self, categories=None, *args, **kwargs):
        self.base_fields["category"].choices = categories
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs["class"] = "form-control"
        self.fields['blur_word'].widget.attrs["class"] = "form-control"
        self.fields['content'].widget.attrs["class"] = "form-control"
        self.fields['category'].widget.attrs["class"] = "form-select"
        # self.fields['category'].widget=forms.widgets.Select(attrs={'class': 'form-control'})
        # self.fields['category'].widget.attrs.update(width='10')
        # for field in self.fields.values():
        #     field.widget.attrs["class"] = "form-control"

            # if field=='category':
        # field.widget.attrs["class"] = "form-control-dropdown"
        # category = forms.CharField(forms.TextInput(attrs={"class":"form-control-dropdown"}))
