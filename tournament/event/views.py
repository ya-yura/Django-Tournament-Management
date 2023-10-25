from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from .models import Event


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', event.id)
    else:
        form = EventForm()

    return render(request, 'event/create_event.html', {'form': form})


def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})
