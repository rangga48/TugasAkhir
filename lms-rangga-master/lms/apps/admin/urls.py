from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('siswa/', include(('apps.admin.siswa.urls','siswa'), namespace="siswa")),
    path('guru/', include(('apps.admin.guru.urls','guru'), namespace="guru")),
    path('jadwal/', include(('apps.admin.jadwal.urls','guru'), namespace="jadwal")),
    path('mata_pelajaran/', include(('apps.admin.mata_pelajaran.urls','mata_pelajaran'), namespace="mata_pelajaran")),
    path('kelas/', include(('apps.admin.kelas.urls','kelas'), namespace="kelas")),
    path('anggota_kelas/', include(('apps.admin.anggota_kelas.urls','anggota_kelas'), namespace="anggota_kelas")),
    path('dashboard/', include(('apps.admin.dashboard.urls','dashboard'), namespace="dashboard")),
]