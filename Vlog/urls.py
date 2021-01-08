from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import Vlog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Vlog.views.vlog, name='vlog'),
    path('article/<slug:slug>/', Vlog.views.post, name='vlogpost'),
    path('post-like/<slug:slug>/', Vlog.views.like, name='vloglike'),
]
