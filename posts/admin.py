from django.contrib import admin
from .models import AddPost


@admin.register(AddPost)
class AddPostAdmin(admin.ModelAdmin):
    list_display = ('title',)