from django.urls import path
import Breed.views as views

urlpatterns = [
    path('breed/', views.getDogBreed, name='getDogBreed'),
]