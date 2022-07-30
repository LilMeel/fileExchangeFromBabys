from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'id', 'uploaded_date', 'count_of_downloads')

admin.site.register(Document)

