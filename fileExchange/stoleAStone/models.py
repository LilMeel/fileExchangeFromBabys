from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_id = models.IntegerField(blank=True)
    description = models.CharField(max_length = 255, blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uploaded_id}::{self.document.name.split('/')[::-1][0]}"

class Blog(models.Model):
    STATUS_CHOICES = (
        ('loading', 'Load'),
        ('uploaded', 'Uploaded'),
    )
    id = models.IntegerField(blank=True, primary_key=True)
    title_of_file = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='uploaded')
    sender = models.ForeignKey(User, related_name='fileExchange', on_delete=models.CASCADE)
    body = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    size = models.BigIntegerField(blank=True, null=True)

class Meta:
    ordering = ('-push',)

def __str__(self):
    return self.title
