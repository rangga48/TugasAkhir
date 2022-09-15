from django.apps import AppConfig

require_login = True
role = "admin"
class GuruConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'guru'
