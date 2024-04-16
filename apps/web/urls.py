from django.urls import path
from apps.web import views

urlpatterns = [
    path('fff/', views.fff),
    path('ggg/', views.ggg),
    path('hhh/', views.hhh),
]
