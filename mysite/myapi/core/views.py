from .models import CrearEvento
from myapi.serializers import EventSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from myapi import serializers

# Create your views here.


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CrearEventoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CrearEvento.objects.all().order_by('-id')
    serializer_class = EventSerializer

class EventList(APIView):

    def get(self, request):
        user = request.user.id
        eventos = CrearEvento.objects.filter(event_user=user)
        serializer = serializers.EventSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)