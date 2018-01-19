# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Screenshot(models.Model):
    Img = models.ImageField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    user = models.ForeignKey(User)
    private = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.url)


