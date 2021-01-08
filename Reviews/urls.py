from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import Reviews.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Reviews.views.reviews, name='review'),
    path('article/<slug:slug>/', Reviews.views.post, name='reviewpost'),
    path('post-like/<slug:slug>/', Reviews.views.like, name='reviewlike'),
]
