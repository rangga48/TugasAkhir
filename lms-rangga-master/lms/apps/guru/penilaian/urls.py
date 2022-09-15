from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('<str:id_jadwal>', main.index, name="index"),
    path('nilai/<str:id_jadwal>/<str:nis>', main.nilai, name="nilai"),
    path('nilai/<str:id_jadwal>/<str:nis>/detail', main.nilai_detail, name="nilai@detail"),
]