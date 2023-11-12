from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from transliterate import translit


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
    cover = models.ImageField(
        upload_to='events/',
        null=True,
        blank=True,
        help_text='Здесь вы можете загрузить обложку для мероприятия.'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(translit(self.name, 'ru', reversed=True))
            date_part = self.date.strftime("%Y%m%d")
            sport_type_part = slugify(self.sport_type)
            combined_slug = f"{base_slug}-{date_part}-{sport_type_part}"
            self.slug = self.get_unique_slug(combined_slug)
        super().save(*args, **kwargs)

    def get_unique_slug(self, base_slug):
        unique_slug = base_slug
        i = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{i}"
            i += 1
        return unique_slug

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
