from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('', main.index, name="index"),
    path('detail/<str:id_kelas>', main.detail, name="detail"),
    path('detail/<str:id_jadwal>/<str:id_kelas>', main.detail_nilai, name="detail_nilai"),
    path('detail/<str:id_kelas>/cetak', main.cetak_rapot, name="cetak_rapot"),
]