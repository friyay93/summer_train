from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list),
    path('', views.power_point)
]
