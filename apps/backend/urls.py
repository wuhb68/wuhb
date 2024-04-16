from django.urls import path
from apps.backend import views
urlpatterns = [
    path('ccc/', views.ccc),
    path('ddd/', views.ddd),
    path('eee/', views.eee),
]