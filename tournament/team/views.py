from django.shortcuts import render, redirect, get_object_or_404
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
            TeamMember.objects.create(team=team, user=request.user)
            # Редирект на страницу команды
            return redirect('team:team_detail', pk=team.pk)
    else:
        form = TeamForm()

    return render(request, 'team/create_team.html', {'form': form})


def team_detail(request, pk):
    team = Team.objects.get(pk=pk)
    members = TeamMember.objects.filter(team=team)
    is_member = members.filter(user=request.user).exists()
    return render(
        request,
        'team/team_detail.html',
        {'team': team, 'members': members, 'is_member': is_member}
    )


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team/team_list.html', {'teams': teams})


@login_required
def join_team(request, invite_link):
    try:
        team = Team.objects.get(invite_link=invite_link)
        user = request.user
        team_member, created = TeamMember.objects.get_or_create(
            team=team, user=user)
        if created:
            # Успешно добавлен новый участник
            return redirect('team:team_detail', team.id)
        else:
            # Пользователь уже является членом команды
            # Здесь вы можете добавить обработку такого случая
            pass
    except Team.DoesNotExist:
        # Обработка случая, если команда с данным инвайт-ссылкой не найдена
        pass

    return HttpResponseRedirect(reverse('team:team_detail', args=[team.id]))


@login_required
def leave_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.user in team.members.user.all():
        team.members.remove(request.user)
        return redirect('team:team_detail', team_id=team.id)

    return redirect('team:team_detail', team_id=team.id)


@login_required
def delete_team(request, pk):
    team = get_object_or_404(Team, pk=pk)

    if request.user == team.captain:
        # Только капитан команды может удалить её
        team.delete()

    # Перенаправьте пользователя на список команд или другую страницу
    return redirect('team:team_list')
