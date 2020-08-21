from django.forms import ModelForm
from .models import CrearEvento
from django.contrib.auth.models import User

class EventForm(ModelForm):
    class Meta:
        model = CrearEvento
        fields = ('event_name', 'event_category', 'event_place', 'event_address', 'event_initial_date', 'event_final_date', 'event_type', 'thumbnail')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
