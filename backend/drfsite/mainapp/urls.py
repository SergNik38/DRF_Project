from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mainapp.views import *

app_name = 'mainapp'

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
