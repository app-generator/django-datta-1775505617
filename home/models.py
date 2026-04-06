# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Systems(models.Model):

    #__Systems_FIELDS__
    serial = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    hostname = models.TextField(max_length=255, null=True, blank=True)
    version = models.TextField(max_length=255, null=True, blank=True)
    raidtype = models.CharField(max_length=255, null=True, blank=True)
    raid_status = models.TextField(max_length=255, null=True, blank=True)
    ipaddrs = models.TextField(max_length=255, null=True, blank=True)

    #__Systems_FIELDS__END

    class Meta:
        verbose_name        = _("Systems")
        verbose_name_plural = _("Systems")


class Boards(models.Model):

    #__Boards_FIELDS__
    system = models.ForeignKey(Systems, on_delete=models.CASCADE)
    serial = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    channel_qty = models.IntegerField(null=True, blank=True)

    #__Boards_FIELDS__END

    class Meta:
        verbose_name        = _("Boards")
        verbose_name_plural = _("Boards")


class Channels(models.Model):

    #__Channels_FIELDS__
    type = models.TextField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    last_activity = models.DateTimeField(blank=True, null=True, default=timezone.now)
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)

    #__Channels_FIELDS__END

    class Meta:
        verbose_name        = _("Channels")
        verbose_name_plural = _("Channels")



#__MODELS__END
