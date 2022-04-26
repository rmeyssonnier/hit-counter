import pytest
from flask import Flask

from app import HitCounterApp


@pytest.fixture()
def app():
    hitcounter_app = HitCounterApp('hitcounter-test')
    app = hitcounter_app.app
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()