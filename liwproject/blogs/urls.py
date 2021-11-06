#urls.py this file is for blog oniy
from django.urls import path
from .views import index
urlpatterns =[
    path('',index)
]