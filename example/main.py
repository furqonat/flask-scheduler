from flask import Flask

from example.utils import scheduler
from example.services import run

app = Flask(__name__)


def application_factory() -> Flask:
    app.config['SCHEDULER_API_INTERVAL'] = 30
    scheduler.init_app(app)
    scheduler.register_job(run, 10)
    return app


if __name__ == '__main__':
    factory = application_factory()
    factory.app_context().push()
    factory.run(debug=True)