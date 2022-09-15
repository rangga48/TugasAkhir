from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('', main.index, name="index"),
    path('agenda/<str:id_jadwal>', main.agenda, name="index@agenda"),
    path('agenda/<str:id_jadwal>/tambah', main.agenda_tambah, name="agenda_tambah"),
    path('agenda/<str:id_jadwal>/tambah/action', main.agenda_tambah_action, name="agenda@tambahaction")
]