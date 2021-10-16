from PyQt5 import QtCore
from lib.window import Login, ShopWindow, Sign_up
import pytest
import yaml


@pytest.fixture
def data():
    with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
        dataes = yaml.safe_load(file)
    return dataes


def test_window_Login(qtbot):
    # Проверяем, что кнопки в окне Login есть и имеют правильный текст
    window = Login()
    assert (window.login_button and window.signup_button_log) and (window.login_button.text() == 'Login' and
                                                                   window.signup_button_log.text() == 'Sign Up')

    # Проверяем, что строки для ввода логина и пароля пустые
    assert window.user_line_log.text() == '' and window.password_line_log.text() == ''

    # Проверяем, открылось ли окно ShopWindow при вводе правильного логина и пароля
    window.user_line_log.setText('admin')
    window.password_line_log.setText('leonid')
    qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
    assert hasattr(window, 'mainwindow')

    # Проверяем, появляется ли окно "неправильный логин"
    window.user_line_log.setText('')
    window.password_line_log.setText('')
    qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
    # Появится окно, которое нужно закрыть вручную
    assert hasattr(window, 'non_username')

    # Проверяем, появляется ли окно "неправильный пароль"
    window.user_line_log.setText('admin')
    window.password_line_log.setText('')
    qtbot.mouseClick(window.login_button, QtCore.Qt.LeftButton)
    # Появится окно, которое нужно закрыть вручную
    assert hasattr(window, 'incorrect_password')


def test_window_Signup(qtbot):
    window = Sign_up()
    # Проверяем, что при вводе логина, который уже есть в системе, появляется нужное окно
    window.user_line.setText('admin')
    window.password_line.setText('')
    qtbot.mouseClick(window.signup_button, QtCore.Qt.LeftButton)
    # Появится окно, которое нужно закрыть вручную
    assert hasattr(window, 'y_username')

    # Проверяем текст кнопок
    assert (window.signup_button.text() == 'Sign Up')


def test_window_ShopWindow(qtbot, data):
    window = ShopWindow('admin', 'leonid')
    # Проверяемм количество кнопок
    assert len(window.buttons) == 6

    # Проверяем текст кнопок
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


def test_buttons_ShopWindow(qtbot, data):
    window = ShopWindow('admin', 'leonid')
    old_data = data
    # Проверяем, что при нажатии на кнопки данные в файле связанные с количеством домов уменьшаются на 1, а данные с
    # количеством купленных домов админа увеличиваются на один
    qtbot.mouseClick(window.button_house_1, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button_house_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button_house_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button_house_4, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button_house_5, QtCore.Qt.LeftButton)
    with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
        new_data = yaml.safe_load(file)
    for i in range(1, 6):
        assert old_data['houses'][i] == (new_data['houses'][i] + 1)
        assert old_data['users']['admin'][i] == (new_data['users']['admin'][i] - 1)
    with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
        yaml.dump(old_data, file, default_flow_style=False)


def test_end_of_houses_ShopWindow(qtbot, data):
    window = ShopWindow('admin', 'leonid')
    old_data = data
    # Проверяем, что когда товар заканчивается, кнопка пропадает
    for _ in range(10):
        qtbot.mouseClick(window.button_house_1, QtCore.Qt.LeftButton)
    assert hasattr(window, 'new_label_house_1')

    for _ in range(10):
        qtbot.mouseClick(window.button_house_2, QtCore.Qt.LeftButton)
    assert hasattr(window, 'new_label_house_2')

    for _ in range(10):
        qtbot.mouseClick(window.button_house_3, QtCore.Qt.LeftButton)
    assert hasattr(window, 'new_label_house_3')

    for _ in range(10):
        qtbot.mouseClick(window.button_house_4, QtCore.Qt.LeftButton)
    assert hasattr(window, 'new_label_house_4')

    for _ in range(10):
        qtbot.mouseClick(window.button_house_5, QtCore.Qt.LeftButton)
    assert hasattr(window, 'new_label_house_5')

    with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
        yaml.dump(old_data, file, default_flow_style=False)
