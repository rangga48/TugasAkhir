"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', include(('apps.admin.urls','admin'), namespace="admin")),
    path('guru/', include(('apps.guru.urls','guru'), namespace="guru")),
    path('siswa/', include(('apps.siswa.urls','siswa'), namespace="siswa")),
    path('login/', include(('apps.login.urls','login'), namespace="login")),
    path('dashboard/', include(('apps.dashboard.urls','dashboard'), namespace="dashboard"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)