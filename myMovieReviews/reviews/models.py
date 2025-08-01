from django.db import models

# Create your models here.

class MovieReview(models.Model):
    GENRE_CHOICES = [
        ('액션', '액션'),
        ('드라마', '드라마'),
        ('코미디', '코미디'),
        ('로맨스', '로맨스'),
        ('스릴러', '스릴러'),
        ('공포', '공포'),
        ('SF', 'SF'),
        ('판타지', '판타지'),
        ('애니메이션', '애니메이션'),
        ('다큐멘터리', '다큐멘터리'),
        ('기타', '기타'),
    ]
    
    STAR_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='영화 제목')
    director = models.CharField(max_length=100, verbose_name='감독')
    cast = models.CharField(max_length=200, verbose_name='주연')
    genre = models.CharField(max_length=20, verbose_name='장르')
    release_year = models.CharField(max_length=50, verbose_name='개봉년도')
    rating = models.CharField(max_length=50, verbose_name='별점')
    running_time = models.CharField(max_length=50, verbose_name='러닝타임(분)')
    review_content = models.TextField(verbose_name='리뷰 내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = '영화 리뷰'
        verbose_name_plural = '영화 리뷰들'
    
    def __str__(self):
        return f"{self.title} ({self.release_year})"
    
    def get_rating_display(self):
        return self.rating
