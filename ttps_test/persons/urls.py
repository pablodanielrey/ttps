
from django.urls import path, include

from . import views

app_name='persons'
urlpatterns = [
    path('', views.index),
    path('detail/<str:person_id>', views.detail, name='detail')
]
