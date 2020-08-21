from .models import CrearEvento
from myapi.serializers import EventSerializer
from rest_framework import viewsets
from myapi import serializers


from django.shortcuts import render, redirect
from django.template import RequestContext
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic import TemplateView
from django.views import View

from .forms import EventForm, UserForm

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

@csrf_exempt
def ListEvents(request):
    user = request.user.id
    queryset = CrearEvento.objects.filter(event_user=user)
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    return render(request, 'page_4.html',{'queryset':queryset})


@csrf_exempt
def DeleteEvent(request, evento_id):
    user = request.user.id
    queryset = CrearEvento.objects.filter(event_user=user)
    try:
        eventos = CrearEvento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        raise Http404
    eventos.delete()
    return redirect("http://172.24.98.167:8080/api/events/")

@csrf_exempt
def UpdateEvent(request, evento_id):  
    user = request.user.id
    usere = request.user
    eventos = CrearEvento.objects.get(event_user=user, id=evento_id) 
    form = EventForm(request.POST, instance = eventos)
    if form.is_valid():
        form.save()
        return redirect("http://172.24.98.167:8080/api/events/")
    return render(request, 'update_event.html',
    {'eventos': eventos, 'formulario':form})

# front
class Auth(FormView):
    template_name = "auth.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("event_list")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Auth, self).dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
        return super(Auth, self).form_valid(form)


class UserAPI2(APIView, TemplateView):
    template_name = "registro.html"

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def EventCreate(request):
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    usere = request.user
    formularioIns = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        evento = CrearEvento(event_name=form['event_name'].value(), event_category=form['event_category'].value(), event_place=form['event_place'].value(), event_address=form['event_address'].value(), event_initial_date=form['event_initial_date'].value(), event_final_date=form['event_final_date'].value(), event_type=form['event_type'].value(), thumbnail=form['thumbnail'].value(),event_user=usere)
        evento.save()
            
        return render(request, 'status_create.html', {'formulario':formularioIns})

    else:
        formularioIns = EventForm()

    return render(request, 'create_event.html', {'formulario':formularioIns})