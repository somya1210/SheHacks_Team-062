from django.urls import path
from . import views
from quiz import views as v

urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', views.article, name='article'),
    path('doctor/', views.doctor, name='doctor'),
    
]
