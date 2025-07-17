from django import forms
from .models import Idea, DevTool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'content', 'image', 'interest', 'devtool']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디어명을 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '아이디어 설명을 입력하세요'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'interest': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'devtool': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '아이디어명',
            'content': '아이디어 설명',
            'image': '이미지',
            'interest': '아이디어 관심도',
            'devtool': '예상 개발툴',
        }

class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'kind', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '개발툴명을 입력하세요'}),
            'kind': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '종류를 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '개발툴 설명을 입력하세요'}),
        }
        labels = {
            'name': '이름',
            'kind': '종류',
            'content': '개발툴 설명',
        } 