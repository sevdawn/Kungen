from django.urls import path
from .views import HomePageView, GalleryPageView

urlpatterns = [
    path('gallery/', GalleryPageView.as_view(), name='gallery'), 
    path('', HomePageView.as_view(), name='home'), 
]