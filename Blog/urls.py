from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import Blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Blog.views.blog, name='blog'),
    path('article/<slug:slug>/', Blog.views.post, name='blogpost'),
    path('post-like/<slug:slug>/', Blog.views.like, name='bloglike'),
]
