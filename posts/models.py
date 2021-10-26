from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AddPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان خبر')
    short_description = models.CharField(
        max_length=400, verbose_name='خلاصه خبر')
    content = RichTextUploadingField(verbose_name='توضیحات')

    # created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    def __str__(self):
        return self.title
