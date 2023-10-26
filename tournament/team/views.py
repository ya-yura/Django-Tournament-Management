from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Team, TeamMember
from .forms import TeamForm
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.captain = request.user
            team.save()
            # Редирект на страницу команды
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm()

    return render(request, 'team/create_team.html', {'form': form})


def team_detail(request, pk):
    team = Team.objects.get(pk=pk)
    members = TeamMember.objects.filter(team=team)
    return render(
        request,
        'team/team_detail.html',
        {'team': team, 'members': members}
    )


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team/team_list.html', {'team': teams})


@login_required
def join_team(request, invite_link):
    try:
        team = Team.objects.get(invite_link=invite_link)
        user = request.user
        if request.user != team.captain:
            team_member, created = TeamMember.objects.get_or_create(
                team=team, user=user)
            if created:
                # Успешно добавлен новый участник
                return redirect('team_detail', team.id)
            else:
                # Пользователь уже является членом команды
                # Здесь вы можете добавить обработку такого случая
                pass
    except Team.DoesNotExist:
        # Обработка случая, если команда с данным инвайт-ссылкой не найдена
        pass

    return HttpResponseRedirect(reverse('team:team_detail', args=[team.id]))
