from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('<str:id_jadwal>', main.index, name="index"),
    path('<str:id_agenda>/submit/<str:id_tugas>/<str:id_jadwal>', main.submit, name="submit")
]