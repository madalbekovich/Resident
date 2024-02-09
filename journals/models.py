from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class Holiday(models.Model):
    img = models.ImageField(upload_to='location-images')
    topic = models.CharField(_('Тема'), max_length=50)
    description = models.TextField(_('Описание'), max_length=120)
    created_at = models.DateTimeField(default=now)
    reading_is = models.IntegerField()

    class Meta:
        verbose_name = 'Роскошный отдых'
        verbose_name_plural = 'Роскошный отдых'

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        if len(self.description.split()) >= 100:
            self.reading_is = f'{1} МИН'
            super().save(*args, **kwargs)


class Estate(models.Model):
    img = models.ImageField(upload_to='location-images')
    topic = models.CharField(_('Тема'), max_length=50)
    description = models.TextField(_('Описание'), max_length=120)
    created_at = models.DateField(default=now)
    reading_is = models.IntegerField()

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        if len(self.description.split()) >= 100:
            self.reading_is = f'{1} МИН'
            super().save(*args, **kwargs)


class Interview(models.Model):
    img = models.ImageField(upload_to='location-images')
    topic = models.CharField(_('Тема'), max_length=50)
    description = models.TextField(_('Описание'), max_length=120)
    created_at = models.DateField(default=now)
    reading_is = models.IntegerField()

    class Meta:
        verbose_name = 'Интервью'
        verbose_name_plural = 'Интервью'

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        if len(self.description.split()) >= 100:
            self.reading_is = f'{1} МИН'
            super().save(*args, **kwargs)




