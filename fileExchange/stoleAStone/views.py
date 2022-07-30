from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from .forms import UploadFileFrom

def mode_form_upload(request):
        if request.method == 'POST':
            form = UploadFileFrom(request.Post, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                form = UploadFileFrom()

            return render(request, 'upload.html', {'form' : form})

