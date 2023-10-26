from django.db import models
from django.contrib.auth.models import User
from event.models import Event
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
import uuid


class Team(models.Model):
    name = models.CharField(_('Название команды'), max_length=100)
    description = models.TextField(_('Описание команды'))
    captain = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Капитан команды'))
    slug = models.SlugField(_('Слаг'), unique=True, blank=True)
    invite_link = models.UUIDField(default=uuid.uuid4, unique=True)

    def save(self, *args, **kwargs):
        if not self.invite_link:
            self.invite_link = uuid.uuid4()
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            i = 1
            while Team.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{i}"
                i += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Команда')
        verbose_name_plural = _('Команды')
        ordering = ('id',)


class TeamMember(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Участник команды'))

    class Meta:
        verbose_name = _('Участник команды')
        verbose_name_plural = _('Участники команды')


class Participant(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name=_('Команда'))
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, verbose_name=_('Мероприятие'))
    rank = models.PositiveIntegerField(_('Ранг'), null=True, blank=True)

    class Meta:
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')
        ordering = ('id',)
