from .models import CrearEvento
from myapi.serializers import EventSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from myapi import serializers
from rest_framework import status

# Create your views here.


class CrearEventoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CrearEvento.objects.all().order_by('-id')
    serializer_class = EventSerializer


class EventList(APIView):
    permission_classes = (IsAuthenticated,)

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

class EventDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, crearevento_id):
        user = request.user.id
        eventos = CrearEvento.objects.filter(
            event_user=user, id=crearevento_id)
        serializer = serializers.EventSerializer(eventos, many=True)
        return Response(serializer.data)

    def put(self, request, crearevento_id):
        user = request.user.id
        eventos = CrearEvento.objects.get(
            event_user=user, id=crearevento_id)
        serializer = serializers.EventSerializer(
            eventos, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            eventos_guardado = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, crearevento_id):
        try:
            eventos = CrearEvento.objects.get(id=crearevento_id)
        except Evento.DoesNotExist:
            raise Http404
        eventos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)