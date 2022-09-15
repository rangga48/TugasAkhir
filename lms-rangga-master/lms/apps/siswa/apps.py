from django.apps import AppConfig

require_login = True
role = "siswa"
class SiswaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siswa'
