from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('<str:id_kelas>', main.index, name="index"),
    path('tambah/<str:id_kelas>', main.tambah, name="tambah"),
    path('hapus/<str:nis>/<str:id_anggota_kelas>/<str:id_kelas>', main.hapus, name="hapus"),
]