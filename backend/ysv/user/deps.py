from .router import app_users


current_admin = app_users.current_user(active=True, superuser=True)
