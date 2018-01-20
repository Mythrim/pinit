# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from pinit.screenshot.models import Screenshot


class ScreenshotView(APIView):

    def post(self,request):
        data = request.POST
        img = data.get('img')
        url = data.get('url')
        try:
            Screenshot.objects.create(img=img, url=url, user=request.user)
            return JsonResponse({"status": "ok"})
        except:
            return JsonResponse({"status": "failed"})


class ScreenshotViewPublic(APIView):

    def get(self,request):
        t = Screenshot.objects.all()
        data = request.GET
        print t[0].img, "HERE"
        return render(request, 'dashboard.html', {'data': t})
