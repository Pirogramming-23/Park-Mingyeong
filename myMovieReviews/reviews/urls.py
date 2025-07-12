from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.MovieReviewListView.as_view(), name='review_list'),
    path('<int:pk>/', views.MovieReviewDetailView.as_view(), name='review_detail'),
    path('create/', views.MovieReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/update/', views.MovieReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', views.delete_review, name='review_delete'),
] 