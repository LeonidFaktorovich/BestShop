from PyQt5 import QtCore
from PyQt5.Qt import *
from lib.window import Login, ShopWindow, No_username
import pytest
import yaml


@pytest.fixture
def data():
    with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
        dataes = yaml.safe_load(file)
    return dataes


def test_buttons_start(qtbot):
    window = Login()
    assert (window.login_button and window.signup_button_log) and (window.login_button.text() == 'Login' and
                                                                   window.signup_button_log.text() == 'Sign Up')


def test_LineEdit_start(qtbot):
    window = Login()
    assert window.user_line_log.text() == '' and window.password_line_log.text() == ''


def test_geometry(qtbot):
    window = ShopWindow('admin', 'leonid')
    assert len(window.buttons) == 6


def test_text_of_buttons(qtbot, data):
    window = ShopWindow('admin', 'leonid')
    string = 'Купить дом первого уровня\nВ наличии: {}'.format(data['houses'][1])
    assert string == window.button_house_1.text()

    string = 'Купить дом второго уровня\nВ наличии: {}'.format(data['houses'][2])
    assert string == window.button_house_2.text()

    string = 'Купить дом третьего уровня\nВ наличии: {}'.format(data['houses'][3])
    assert string == window.button_house_3.text()

    string = 'Купить дом четвертого уровня\nВ наличии: {}'.format(data['houses'][4])
    assert string == window.button_house_4.text()

    string = 'Купить дом пятого уровня\nВ наличии: {}'.format(data['houses'][5])
    assert string == window.button_house_5.text()

    string = 'Показать покупки'
    assert string == window.button_of_stat.text()


# Проверяем, открылось ли окно ShopWindow
def test_buttons_login(qtbot, data):
    window = Login()
    window.user_line_log.setText('admin')
    window.password_line_log.setText('leonid')
    qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
    assert hasattr(window, 'mainwindow')

def test_login_error(qtbot):
    window = Login()
    window.user_line_log.setText('')
    window.password_line_log.setText('')
    qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
    window.non_username.done(1)
    assert hasattr(window, 'non_username')
def test_password_error(qtbot):
    window = Login()
    window.user_line_log.setText('admin')
    window.password_line_log.setText('')
    qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
    assert hasattr(window, 'incorrect_password')



