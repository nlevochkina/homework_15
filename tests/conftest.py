import pytest
from selene import browser


@pytest.fixture(params=[('1920', '1080'), ('1280', '832')], scope='function')
def setup_browser_desktop_version(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[('360', '800'), ('700', '960')], scope='function')
def setup_browser_mobile_version(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[('1920', '1080'), ('700', '960')], scope='function')
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if int(height) == 1080:
        yield 'desktop_version'
    else:
        yield 'mobile_version'
    browser.quit()
