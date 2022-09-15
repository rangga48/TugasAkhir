from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('jadwal/', include(('apps.siswa.jadwal.urls','jadwal'), namespace="jadwal")),
    path('materi/', include(('apps.siswa.materi.urls','materi'), namespace="materi")),
    path('tugas/', include(('apps.siswa.tugas.urls','tugas'), namespace="tugas")),
    path('rapot/', include(('apps.siswa.rapot.urls','rapot'), namespace="rapot")),
]
