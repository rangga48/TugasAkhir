from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('', main.index, name="index"),
    path('tambah/', main.tambah, name="tambah"),
    path('ubah/<str:nis>', main.ubah, name="ubah"),
    path('hapus/<str:nis>', main.hapus, name="hapus"),
]