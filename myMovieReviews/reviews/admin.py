from django.contrib import admin
from .models import MovieReview

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'genre', 'release_year', 'rating', 'created_at']
    list_filter = ['genre', 'rating', 'release_year', 'created_at']
    search_fields = ['title', 'director', 'cast', 'review_content']
    list_per_page = 20
    ordering = ['-created_at']
    
    fieldsets = (
        ('영화 정보', {
            'fields': ('title', 'director', 'cast', 'genre', 'release_year', 'running_time')
        }),
        ('평가', {
            'fields': ('rating', 'review_content')
        }),
        ('메타데이터', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
