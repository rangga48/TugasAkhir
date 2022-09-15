from django.apps import AppConfig

require_login = True
role = "admin"
class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin'
