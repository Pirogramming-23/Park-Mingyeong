from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('like-toggle/', views.like_toggle, name='like_toggle'),
    path('comment-add/', views.comment_add, name='comment_add'),
    path('comment-delete/', views.comment_delete, name='comment_delete'),
] 