from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # To import signal add below method.
    def ready(self):
        import users.signals
