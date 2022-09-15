from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('<str:id_agenda>', main.index, name="index"),
    path('<str:id_agenda>/tambah', main.tambah, name="tambah"),
    path('<str:id_agenda>/ubah/<str:id_materi>', main.ubah, name="ubah"),
    path('<str:id_agenda>/hapus/<str:id_materi>', main.hapus, name="hapus"),
]