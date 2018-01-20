# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageField
# Create your models here.
from storages.backends.s3boto import S3BotoStorage

from pinit.settings.common import AWS_STORAGE_BUCKET_NAME


def get_storage_path(instance, filename):
    '''
        This function defines the path where the file needs to be stored. Also file name
        is changed while storing the file
    '''

    if instance.img:
        extension = instance.img.file.name.split(".")[-1]
        username = str(instance.user.username)
        current_time = str(datetime.now().strftime('%H:%M:%S'))
        file_name = username + '/' + '-' + current_time + '.' + extension
        path = os.path.join('')
    return path + '/{}'.format(file_name)

class Screenshot(models.Model):
    img = models.FileField(null=True,blank=True,upload_to=get_storage_path, storage=S3BotoStorage(bucket=AWS_STORAGE_BUCKET_NAME))
    url = models.URLField(null=True,blank=True)
    user = models.ForeignKey(User)
    private = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.url)


