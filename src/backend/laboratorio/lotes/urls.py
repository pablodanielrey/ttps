
from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('lotes', views.VistaLotes)


urlpatterns = [
    path('estudios', views.VistaEstudios.as_view())
]
urlpatterns.extend(router.urls)