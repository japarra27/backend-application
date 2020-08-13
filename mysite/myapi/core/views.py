from .models import CrearEvento
from myapi.serializers import EventSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

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
