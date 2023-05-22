from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    cotent_upload = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Talks(models.Model):
    title = models.CharField(max_length=255)
    vedio = models.FileField(upload_to='vedio/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Academy(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    img = models.ImageField(upload_to='img/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

