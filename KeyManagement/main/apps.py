from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    # def ready(self):
    #     from jobs.updater import schedule_key_deletion
    #     schedule_key_deletion()
