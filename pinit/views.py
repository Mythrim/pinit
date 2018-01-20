from __future__ import unicode_literals, absolute_import
from django.http.response import HttpResponse
from django.shortcuts import render
import datetime


def health_check(request):
    return HttpResponse("OK", status=200)



