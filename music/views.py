from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Songs
from .serializer import SongsSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class SongsList(APIView):

    def get(self, request):
        param_value = request.GET.get('id')
        search_key = request.GET.get('search')

        if param_value != None:
            song = Songs.objects.get(uid=param_value)
            serializer = SongsSerializer(song)
            return Response({"Song": serializer.data})

        if search_key != None:
            filter_song = Songs.objects.filter(title__contains=search_key) 
            serializer = SongsSerializer(filter_song, many=True)
            return Response({"Song": serializer.data})

        songs = Songs.objects.all().order_by('title')
        serializer = SongsSerializer(songs, many=True)
        return Response({"Songs": serializer.data})
    
    def post(self,request):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("ENTRY CERATED", status=status.HTTP_201_CREATED)
        # Songs.objects.create(title=title,artist=artist)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        songs = Songs.objects.all()
        for song in songs:
            if song.uid == (request.data).get('uid'):
                song.artist = (request.data).get('artist')
                song.save()
                return Response("ENTRY UPDATED", status=status.HTTP_200_OK)
        return Response("Not updated", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        songs = Songs.objects.all()
        for song in songs:
            if song.uid == (request.data).get('uid'):
                song.delete()
                return Response("ENTRY DELETED", status=status.HTTP_200_OK)


    
