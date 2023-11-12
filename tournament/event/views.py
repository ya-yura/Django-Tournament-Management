from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .models import Event
from .forms import EventForm
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
        return redirect('event:event_detail', obj.slug)

    logger.error(f"Ошибка: {form.errors}")
    context = {'form': form, 'is_edit': False}
    return render(request, template, context)


def event_detail(request, slug):
    if not slug:
        return HttpResponseNotFound("Страница не найдена")

    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event/event_detail.html', {'event': event})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})
