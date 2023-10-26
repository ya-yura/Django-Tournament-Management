from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time',
                  'sport_type', 'location', 'team_limit']

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
