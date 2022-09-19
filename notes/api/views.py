from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Noteserializer
from .models import Note
# Create your views here.


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getRoutes(request):
    routes = [

        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,


        },
        {
            'Endpoint': '/notes/id/',
            'method': 'GET',
            'body': None,

        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},

        },
        {
            'Endpoint': '/notes/update/',
            'method': 'PUT',
            'body': {'body': ""},

        },
        {
            'Endpoint': '/notes/delete/',
            'method': 'DELTE',
            'body': None,

        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    note = Note.objects.all()
    serializer = Noteserializer(note, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, id):
    note = Note.objects.get(id=id)
    serializer = Noteserializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = Noteserializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def UpdateNote(request, id):
    data = request.data
    note = Note.objects.get(id=id)
    serializer = Noteserializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response("Note was deleted!!")
