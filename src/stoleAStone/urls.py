from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main, name='show_main'),
#    path('count/<pk>/', downloaded_count, name='downloaded_count')
]