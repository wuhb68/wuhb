from django.urls import path
from apps.api import views

urlpatterns = [
    path('index/', views.index),
    path('aaa/', views.aaa),
    path('bbb/', views.bbb),
]
