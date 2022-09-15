from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('', main.index, name="index"),
    path('tambah/', main.tambah, name="tambah"),
    path('hapus/<str:id_jadwal>', main.hapus, name="hapus"),
]