from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('filladminform/',views.filladminform,name='filladminform'),
    path('search/',views.start_crawl,name='search'),
]
