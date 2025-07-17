from django.contrib import admin
from .models import DevTool, Idea, IdeaStar

@admin.register(DevTool)
class DevToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'created_at')
    list_filter = ('kind', 'created_at')
    search_fields = ('name', 'content')
    ordering = ('-created_at',)

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'devtool', 'interest', 'created_at')
    list_filter = ('devtool', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

@admin.register(IdeaStar)
class IdeaStarAdmin(admin.ModelAdmin):
    list_display = ('idea', 'user', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
