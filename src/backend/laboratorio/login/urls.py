

from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.VistaToken.as_view()),
    path('roles/', views.VistaRoles.as_view()),
]

for u in urlpatterns:
    print(u)