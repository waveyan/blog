from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def myvalidator(value):
    if len(value)>2:
        raise ValidationError(
            _('太长了，短一点！'),
        )

class User(AbstractUser):
    nickname=models.CharField(max_length=50,blank=True,validators=[myvalidator])

    class Meta(AbstractUser.Meta):
        pass


