#urls.py this file is for blog oniy
from django.urls import path
from .views import index
from .views import blogDetail
urlpatterns =[
    path('',index),
    path('blog/<int:id>',blogDetail,name="blogDetail")
]