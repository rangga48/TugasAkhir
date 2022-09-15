from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import main
urlpatterns = [
    path('<str:id_agenda>', main.index, name="index"),
    path('<str:id_agenda>/post', main.absensi, name="index@absensi"),
]