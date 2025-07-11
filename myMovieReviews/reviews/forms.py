from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'director', 'cast', 'genre', 'release_year', 'rating', 'running_time', 'review_content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'cast': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
            'running_time': forms.TextInput(attrs={'class': 'form-control'}),
            'review_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
        labels = {
            'title': '영화 제목',
            'director': '감독',
            'cast': '주연',
            'genre': '장르',
            'release_year': '개봉년도',
            'rating': '별점',
            'running_time': '러닝타임 (분)',
            'review_content': '리뷰 내용',
        } 