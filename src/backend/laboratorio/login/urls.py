

from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.VistaToken.as_view())
]

for u in urlpatterns:
    print(u)