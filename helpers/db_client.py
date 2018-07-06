class Router:
    """
    A router to control all database operations on models in the
    client application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read client models go to client_db.
        """
        if model._meta.app_label == 'client':
            return 'client_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write client models go to client_db.
        """
        if model._meta.app_label == 'client':
            return 'client_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the client app is involved.
        """
        if obj1._meta.app_label == 'client' or \
           obj2._meta.app_label == 'client':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the client app only appears in the 'client_db'
        database.
        """
        if app_label == 'client':
            return db == 'client_db'
        return None
