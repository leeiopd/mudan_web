from django import forms
from .models import Notice
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'name', 'content' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', rows=1),
        )