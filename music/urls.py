from django.urls import path
from .views import SongsList

urlpatterns = [
    path('songs/', SongsList.as_view(), name="songs-all")
]