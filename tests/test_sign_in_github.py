"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.mark.parametrize('setup_browser_desktop_version', [('1920', '1080')], indirect=True)
def test_sign_in_github_desktop(setup_browser_desktop_version):
    browser.open('https://github.com/')
    browser.all('[href="/login"]').second.click()


@pytest.mark.parametrize('setup_browser_mobile_version', [('360', '800')], indirect=True)
def test_sign_in_github_mobile(setup_browser_mobile_version):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.position-relative').click()


def test_sign_in_github_desktop_skip(setup_browser):
    if setup_browser == 'desktop_version':
        pytest.skip('Настройка для десктопной версии')
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.position-relative').click()


def test_sign_in_github_mobile_skip(setup_browser):
    if setup_browser == 'mobile_version':
        pytest.skip('Настройка для мобильной версии')
    browser.open('https://github.com/')
    browser.all('[href="/login"]').second.click()
