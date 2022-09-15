from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('', main.index, name="index"),
    path('tambah/', main.tambah, name="tambah"),
    path('ubah/<str:id_guru>', main.ubah, name="ubah"),
    path('hapus/<str:id_guru>', main.hapus, name="hapus"),
]