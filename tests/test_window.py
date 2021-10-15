from PyQt5 import QtCore
from lib.window import Login
import pytest
import yaml

@pytest.fixture
def data():
    with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
        dataes = yaml.safe_load(file)
    print(dataes)
    return dataes
def test_buttons_start(qtbot):
    window = Login()
    assert (window.login_button and window.signup_button_log) and (window.login_button.text() == 'Login' and
                                                                   window.signup_button_log.text() == 'Sign Up')

def test_LineEdit_start(qtbot):
    window = Login()
    assert window.user_line_log.text() == '' and window.password_line_log.text() == ''

def test_login(qtbot):
    window = Login()
    for name in data['users']:
        password = name['password']
        window.user_line_log.text(name)
        window.password_line_log.text(password)
        qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
