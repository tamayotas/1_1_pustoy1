from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def test1():
    browser.open('https://google.com')
    print ("Я выполняюсь перед тестом. Открывается браузер")

    yield "Browser"

    # print ("Я выполняюсь после теста. Закрывается браузер")


@pytest.fixture
def test2():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    pass

    yield "Line"

def test_contains_text(test1, test2):
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_contains_text1():
    return "Takogo texta net"

def test_text(test_contains_text, test_contains_text1):
    assert test_contains_text == "Takogo texta net"