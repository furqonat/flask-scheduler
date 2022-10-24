import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


class Scheduler(object):

    def __init__(self, app: Flask = None) -> None:
        self.scheduler = BackgroundScheduler(daemon=True)
        self.jobs = []
        self._runner = None
        self._interval = 60
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask = None) -> None:
        """
        Initialize the application for use with this

        :param app:
            The Flask application object
        """
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['scheduler'] = self
        self._default_configuration(app)

        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())
        self._interval = app.config['SCHEDULER_API_INTERVAL']
        self.scheduler.add_job(self._run, 'interval', seconds=self._interval)

        @app.teardown_appcontext
        def shutdown():
            self.scheduler.shutdown()
            atexit.unregister(lambda: self.scheduler.shutdown())

    @staticmethod
    def _default_configuration(app: Flask) -> None:
        """
        Set default configuration values for the application.

        :param app:
            The Flask application object
        :return: None
        """
        app.config.setdefault('SCHEDULER_API_INTERVAL', 30)

    def _run(self):
        for job in self.jobs:
            job()

    def runner(self):
        def decorator(f):
            if not hasattr(self, 'jobs'):
                self.jobs = []
            self.jobs.append(f)
            return f

        return decorator
