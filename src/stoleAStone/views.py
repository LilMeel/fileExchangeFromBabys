from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.http import FileResponse

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


def downloaded_count(request, pk):
    '''Счетчик клика по ссылке, на определённый файл'''
    pass
    # try:
    #     price = get_object_or_404(PriceList, is_active=True)
    # except MultipleObjectsReturned:
    #     return HttpResponse('Вы выбрали более одного файла')
    #clicked = UploadFileFrom.objects.get(pk=pk)
    #clicked.counter += 1
    #clicked.save()
    #return redirect(clicked.file.url)

def show_main(request):
    return render(request, 'index.html', {})

