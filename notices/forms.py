from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Notice
		fields = ['title', 'content']