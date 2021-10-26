from django import urls
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Scrapy Django Project"
admin.site.site_title = "Scrapy Django Project"
admin.site.index_title = "Scrapy Django Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
