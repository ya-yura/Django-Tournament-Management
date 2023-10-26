from django.contrib import admin
from .models import Team, Participant


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'team', 'rank')
    search_fields = ('user__username', 'event__name')
    ordering = ('user__username', 'event__name')
