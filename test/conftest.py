import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    if not fixture.is_valid():
        fixture = Application()
        fixture.session.login(username="admin", password="secret")

    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request, app):
    def fin():
        app.session.logout()
        app.destroy()

    request.addfinalizer(fin)
