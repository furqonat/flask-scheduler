from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Scheduler(object):

    def __init__(self, app: Flask = None, db: SQLAlchemy = None) -> None:
        if app is not None and db is not None:
            self.db = db
            self.init_app(app)

    def init_app(self, app: Flask = None, db: SQLAlchemy = None) -> None:
        """
        Initialize the application for use with this

        :param app:
            The Flask application object
        :param db:
            The SQLAlchemy database object
        """
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['scheduler'] = self
        self.db = db or self.db

    @staticmethod
    def _default_configuration(app: Flask) -> None:
        """
        Set default configuration values for the application.

        :param app:
            The Flask application object
        :return: None
        """
        app.config.setdefault('SCHEDULER_API_INTERVAL', 30)
