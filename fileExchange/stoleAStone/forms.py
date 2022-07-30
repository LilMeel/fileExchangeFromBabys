from django import forms
from models import Document

class UploadFileFrom(forms.Form):
    class Meta:
        model = Document
        fields = ('document', 'uploaded_id', 'description', 'uploaded_at')