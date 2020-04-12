from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'Home'

    def ready(self):
        import os
        from . import jobs

        # RUN_MAIN check to avoid running the code twice since manage.py runserver runs 'ready' twice on startup
        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start()
