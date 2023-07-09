from django.db import models, transaction
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Fan(models.Model):

    name = models.CharField(
        max_length=36,
    )
    slug = models.SlugField(
        max_length=50,
        db_index=True,
        unique=True,
        editable=False,
    )

    DIRECTION__FORWARD = 0
    DIRECTION__REVERSE = 1

    _direction_state = models.IntegerField(
        choices=(
            (DIRECTION__FORWARD, _("Forward")),
            (DIRECTION__REVERSE, _("Reverse")),
        ),
        default=DIRECTION__FORWARD,
    )

    SPEED__OFF = 0
    SPEED__SLOW = 1
    SPEED__MEDIUM = 2
    SPEED__FAST = 3

    _speed_state = models.IntegerField(
        choices=(
            (SPEED__OFF, _("Off")),
            (SPEED__SLOW, _("Slow")),
            (SPEED__MEDIUM, _("Medium")),
            (SPEED__FAST, _("Fast")),
        ),
        default=SPEED__OFF,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if Fan.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{(Fan.objects.filter(slug__startswith=self.slug).count() + 1)}"
        super().save(*args, **kwargs)


    @property
    def speed_state(self):
        self.refresh_from_db()
        return self._speed_state

    @property
    def direction_state(self):
        self.refresh_from_db()
        return self._direction_state

    def speed_next(self):
        with transaction.atomic():
            # select_for_update ensures the value cannot be updated by anything other than this codeblock
            fan = Fan.objects.select_for_update().get(pk=self.pk)
            # addition by 1, combined with modulus operator ensure correct state sequence
            fan._speed_state = (fan._speed_state + 1) % 4
            fan.save(update_fields=['_speed_state'])

    def direction_next(self):
        with transaction.atomic():
            fan = Fan.objects.select_for_update().get(pk=self.pk)
            fan._direction_state = (fan._direction_state + 1) % 2
            fan.save(update_fields=['_direction_state'])
