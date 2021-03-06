"""pinit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals, absolute_import

from .screenshot.views import ScreenshotView, ScreenshotViewPublic

from .screenshot.views import ScreenshotViewPrivate
from . import views

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .authentication.views import UserViewSet
from .authentication import urls as authentication_urls

router = DefaultRouter()
router.register(r'users', UserViewSet)

schema_view = get_swagger_view(title='pinit APIs')

from rest_auth import urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^swagger/$', schema_view),
    #url(r'^api/v1/', include(authentication_urls)),
    #url(r'^api/v1/', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^screenshot/',ScreenshotView.as_view()),
    url(r'^public/', ScreenshotViewPublic.as_view()),
     url(r'^private/', ScreenshotViewPrivate.as_view()),
    url(r'^healthcheck/$', views.health_check),
]

