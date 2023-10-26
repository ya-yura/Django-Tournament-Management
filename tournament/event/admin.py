from django.contrib import admin
from .models import Event, Tournament


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'sport_type', 'location')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'status', 'bracket_type')
    search_fields = ('name',)
    ordering = ('name',)
