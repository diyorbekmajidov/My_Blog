from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    cotent_upload = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title
