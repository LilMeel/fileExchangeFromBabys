from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_id = models.IntegerField(blank=True)
    counter = models.PositiveIntegerField(default=0, verbose_name='Кол-во загрузок')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uploaded_id}::{self.document.name.split('/')[::-1][0]}"

