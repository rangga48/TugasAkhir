from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('<str:id_agenda>', main.index, name="index"),
    path('<str:id_agenda>/tambah', main.tambah, name="tambah"),
    path('<str:id_agenda>/ubah/<str:id_tugas>', main.ubah, name="ubah"),
    path('<str:id_agenda>/hapus/<str:id_tugas>', main.hapus, name="hapus"),
    path('pengerjaan/<str:id_tugas>', main.pengerjaan, name="pengerjaan"),
    path('pengerjaan/<str:id_tugas>/approve/<str:id_tugas_pengerjaan>', main.approve, name="approve"),
]