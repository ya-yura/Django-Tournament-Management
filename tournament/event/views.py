from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from .models import Event
import logging

logger = logging.getLogger(__name__)


@login_required
def create_event(request):
    template = 'event/create_event.html'
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        logger.info(f"Мероприятие создано: {obj}")
        return redirect('event:event_detail', obj.id)

    logger.error(f"Ошибка: {form.errors}")
    context = {'form': form, 'is_edit': False}
    return render(request, template, context)


def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})
