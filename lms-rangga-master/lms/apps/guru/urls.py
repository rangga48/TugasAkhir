from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('jadwal/', include(('apps.guru.jadwal.urls','jadwal'), namespace="jadwal")),
    path('materi/', include(('apps.guru.materi.urls','materi'), namespace="materi")),
    path('tugas/', include(('apps.guru.tugas.urls','tugas'), namespace="tugas")),
    path('penilaian/', include(('apps.guru.penilaian.urls','ujian'), namespace="penilaian")),
    
    path('absensi/', include(('apps.guru.absensi.urls','absensi'), namespace="absensi")),
]