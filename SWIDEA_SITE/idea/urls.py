from django.urls import path
from . import views

app_name = 'idea'

urlpatterns = [
    # 아이디어 관련 URL
    path('', views.idea_list, name='idea_list'),
    path('idea/create/', views.idea_create, name='idea_create'),
    path('idea/<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('idea/<int:idea_id>/edit/', views.idea_edit, name='idea_edit'),
    path('idea/<int:idea_id>/delete/', views.idea_delete, name='idea_delete'),
    
    # 개발툴 관련 URL
    path('devtool/', views.devtool_list, name='devtool_list'),
    path('devtool/create/', views.devtool_create, name='devtool_create'),
    path('devtool/<int:devtool_id>/', views.devtool_detail, name='devtool_detail'),
    path('devtool/<int:devtool_id>/edit/', views.devtool_edit, name='devtool_edit'),
    path('devtool/<int:devtool_id>/delete/', views.devtool_delete, name='devtool_delete'),
    
    # 찜하기 URL
    path('star/<int:idea_id>/', views.toggle_star, name='toggle_star'),
    
    # 관심도 조절 URL
    path('interest/<int:idea_id>/<str:action>/', views.change_interest, name='change_interest'),
] 