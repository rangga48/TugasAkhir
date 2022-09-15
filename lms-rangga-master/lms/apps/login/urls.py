from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('auth/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
]