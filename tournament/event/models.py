from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


SPORT_CHOICES = [
    ('football', 'Футбол'),
    ('basketball', 'Баскетбол'),
    ('tennis', 'Теннис'),
    # Добавьте другие виды спорта, которые вам необходимы
]


class Event(models.Model):
    name = models.CharField(_('Название мероприятия'), max_length=100)
    description = models.TextField(_('Описание мероприятия'))
    date = models.DateField(_('Дата мероприятия'))
    time = models.TimeField(_('Время мероприятия'))
    sport_type = models.CharField(
        _('Тип спорта'), max_length=50, choices=SPORT_CHOICES)
    location = models.CharField(_('Местоположение'), max_length=100)
    team_limit = models.PositiveIntegerField(_('Лимит команд'))
    slug = models.SlugField(_('Слаг'), unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Организатор'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')
        ordering = ('id',)


class Tournament(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, verbose_name=_('Мероприятие'))
    name = models.CharField(_('Название турнира'), max_length=100)
    description = models.TextField(_('Описание турнира'))
    date = models.DateTimeField(_('Дата и время турнира'))
    status = models.CharField(_('Статус турнира'), max_length=20)
    bracket_type = models.CharField(_('Тип сетки'), max_length=20)
    prizes = models.TextField(_('Призы'))

    class Meta:
        verbose_name = _('Турнир')
        verbose_name_plural = _('Турниры')
        ordering = ('id',)
