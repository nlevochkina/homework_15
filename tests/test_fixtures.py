"""
Фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser


def test_github_desktop_version(setup_browser_desktop_version):
    browser.open("https://github.com/")
    browser.all('[href="/login"]').second.click()


def test_github_mobile_version(setup_browser_mobile_version):
    browser.open("https://github.com/")
    browser.element('.Button-label').click()
    browser.element('.position-relative').click()