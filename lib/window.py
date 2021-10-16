import yaml
from PyQt5.Qt import *


class ShopWindow(QMainWindow):

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.setWindowTitle('Колонизация Марса')

        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
            self.data = yaml.safe_load(file)

        self.buttons = []
        # дом 1
        self.pixmap_1 = QPixmap('/Users/apple/PycharmProjects/BestShop/lib/photo_2.jpeg')
        self.label_house_1 = QLabel(self)
        self.label_house_1.setPixmap(self.pixmap_1)
        self.label_house_1.setGeometry(300, 50, 200, 200)
        self.button_house_1 = QPushButton('Купить дом первого уровня\nВ наличии: {}'
                                          .format(self.data['houses'][1]), self)
        self.button_house_1.setGeometry(275, 270, 250, 80)
        self.button_house_1.clicked.connect(self.on_click)
        self.buttons.append(self.button_house_1)
        # дом 2
        self.pixmap_2 = QPixmap('/Users/apple/PycharmProjects/BestShop/lib/photo_2.jpeg')
        self.label_house_2 = QLabel(self)
        self.label_house_2.setPixmap(self.pixmap_2)
        self.label_house_2.setGeometry(675, 50, 200, 200)

        self.button_house_2 = QPushButton('Купить дом второго уровня\nВ наличии: {}'
                                          .format(self.data['houses'][2]), self)
        self.button_house_2.setGeometry(650, 270, 250, 80)
        self.button_house_2.clicked.connect(self.on_click_2)
        self.buttons.append(self.button_house_2)
        # дом 3
        self.pixmap_3 = QPixmap('/Users/apple/PycharmProjects/BestShop/lib/photo_2.jpeg')
        self.label_house_3 = QLabel(self)
        self.label_house_3.setPixmap(self.pixmap_3)
        self.label_house_3.setGeometry(1050, 50, 200, 200)

        self.button_house_3 = QPushButton('Купить дом третьего уровня\nВ наличии: {}'
                                          .format(self.data['houses'][3]), self)
        self.button_house_3.setGeometry(1025, 270, 250, 80)
        self.button_house_3.clicked.connect(self.on_click_3)
        self.buttons.append(self.button_house_3)
        # дом 4
        self.pixmap_4 = QPixmap('/Users/apple/PycharmProjects/BestShop/lib/photo_2.jpeg')
        self.label_house_4 = QLabel(self)
        self.label_house_4.setPixmap(self.pixmap_4)
        self.label_house_4.setGeometry(300, 400, 200, 200)
        self.button_house_4 = QPushButton('Купить дом четвертого уровня\nВ наличии: {}'
                                          .format(self.data['houses'][4]), self)
        self.button_house_4.setGeometry(275, 620, 250, 80)
        self.button_house_4.clicked.connect(self.on_click_4)
        self.buttons.append(self.button_house_4)
        # дом 5
        self.pixmap_5 = QPixmap('/Users/apple/PycharmProjects/BestShop/lib/photo_2.jpeg')
        self.label_house_5 = QLabel(self)
        self.label_house_5.setPixmap(self.pixmap_5)
        self.label_house_5.setGeometry(675, 400, 200, 200)
        self.button_house_5 = QPushButton('Купить дом пятого уровня\nВ наличии: {}'
                                          .format(self.data['houses'][5]), self)
        self.button_house_5.setGeometry(650, 620, 250, 80)
        self.button_house_5.clicked.connect(self.on_click_5)
        self.buttons.append(self.button_house_5)
        # Кнопка статистики

        self.button_of_stat = QPushButton('Показать покупки', self)
        self.button_of_stat.setGeometry(50, 125, 170, 50)
        self.button_of_stat.clicked.connect(self.on_click_stat)
        self.buttons.append(self.button_of_stat)

        if self.data['houses'][1] == 0:
            self.button_house_1.hide()
            self.new_label_house_1 = QLabel('Дома первого уровня нет в наличии', self)
            self.new_label_house_1.setGeometry(285, 270, 250, 80)
            self.new_label_house_1.show()

        if self.data['houses'][2] == 0:
            self.button_house_2.hide()
            self.new_label_house_2 = QLabel('Дома второго уровня нет в наличии', self)
            self.new_label_house_2.setGeometry(660, 270, 250, 80)
            self.new_label_house_2.show()

        if self.data['houses'][3] == 0:
            self.button_house_3.hide()
            self.new_label_house_3 = QLabel('Дома третьего уровня нет в наличии', self)
            self.new_label_house_3.setGeometry(1035, 270, 250, 80)
            self.new_label_house_3.show()

        if self.data['houses'][4] == 0:
            self.button_house_4.hide()
            self.new_label_house_4 = QLabel('Дома четвертого уровня нет в наличии', self)
            self.new_label_house_4.setGeometry(275, 620, 250, 80)
            self.new_label_house_4.show()

        if self.data['houses'][5] == 0:
            self.button_house_5.hide()
            self.new_label_house_5 = QLabel('Дома пятого уровня нет в наличии', self)
            self.new_label_house_5.setGeometry(665, 620, 250, 80)
            self.new_label_house_5.show()

        self.resize(1300, 800)
        self.show()

    def on_click(self):
        self.data['houses'][1] -= 1
        self.button_house_1.setText('Купить дом первого уровня\nВ наличии: {}'.format(self.data['houses'][1]))
        if self.data['houses'][1] == 0:
            self.button_house_1.hide()
            self.new_label_house_1 = QLabel('Дома первого уровня нет в наличии', self)
            self.new_label_house_1.setGeometry(285, 270, 250, 80)
            self.new_label_house_1.show()
        self.data['users'][self.username][1] += 1
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
            yaml.dump(self.data, file, default_flow_style=False)

    def on_click_2(self):
        self.data['houses'][2] -= 1
        self.button_house_2.setText('Купить дом второго уровня\nВ наличии: {}'.format(self.data['houses'][2]))
        if self.data['houses'][2] == 0:
            self.button_house_2.hide()
            self.new_label_house_2 = QLabel('Дома второго уровня нет в наличии', self)
            self.new_label_house_2.setGeometry(660, 270, 250, 80)
            self.new_label_house_2.show()
        self.data['users'][self.username][2] += 1
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
            yaml.dump(self.data, file, default_flow_style=False)

    def on_click_3(self):
        self.data['houses'][3] -= 1
        self.button_house_3.setText('Купить дом третьего уровня\nВ наличии: {}'.format(self.data['houses'][3]))
        if self.data['houses'][3] == 0:
            self.button_house_3.hide()
            self.new_label_house_3 = QLabel('Дома третьего уровня нет в наличии', self)
            self.new_label_house_3.setGeometry(1035, 270, 250, 80)
            self.new_label_house_3.show()
        self.data['users'][self.username][3] += 1
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
            yaml.dump(self.data, file, default_flow_style=False)

    def on_click_4(self):
        self.data['houses'][4] -= 1
        self.button_house_4.setText('Купить дом четвертого уровня\nВ наличии: {}'.format(self.data['houses'][4]))
        if self.data['houses'][4] == 0:
            self.button_house_4.hide()
            self.new_label_house_4 = QLabel('Дома четвертого уровня нет в наличии', self)
            self.new_label_house_4.setGeometry(275, 620, 250, 80)
            self.new_label_house_4.show()
        self.data['users'][self.username][4] += 1
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
            yaml.dump(self.data, file, default_flow_style=False)

    def on_click_5(self):
        self.data['houses'][5] -= 1
        self.button_house_5.setText('Купить дом пятого уровня\nВ наличии: {}'.format(self.data['houses'][5]))
        if self.data['houses'][5] == 0:
            self.button_house_5.hide()
            self.new_label_house_5 = QLabel('Дома пятого уровня нет в наличии', self)
            self.new_label_house_5.setGeometry(665, 620, 250, 80)
            self.new_label_house_5.show()
        self.data['users'][self.username][5] += 1
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
            yaml.dump(self.data, file, default_flow_style=False)

    def on_click_stat(self):
        self.stats = Stats(self.username, self.data)


class Stats(QMessageBox):
    def __init__(self, username, data):
        super().__init__()
        if data['users'][username][1] > 4 or data['users'][username][1] == 0:
            self.string_1 = 'домов'
        elif data['users'][username][1] == 1:
            self.string_1 = 'дом'
        else:
            self.string_1 = 'дома'
        if data['users'][username][2] > 4 or data['users'][username][2] == 0:
            self.string_2 = 'домов'
        elif data['users'][username][2] == 1:
            self.string_2 = 'дом'
        else:
            self.string_2 = 'дома'
        if data['users'][username][3] > 4 or data['users'][username][3] == 0:
            self.string_3 = 'домов'
        elif data['users'][username][3] == 1:
            self.string_3 = 'дом'
        else:
            self.string_3 = 'дома'
        if data['users'][username][4] > 4 or data['users'][username][4] == 0:
            self.string_4 = 'домов'
        elif data['users'][username][4] == 1:
            self.string_4 = 'дом'
        else:
            self.string_4 = 'дома'
        if data['users'][username][5] > 4 or data['users'][username][5] == 0:
            self.string_5 = 'домов'
        elif data['users'][username][5] == 1:
            self.string_5 = 'дом'
        else:
            self.string_5 = 'дома'
        self.msg = QMessageBox.information(self, 'Привет!',
                                           'Вы уже купили:\n{} {} первого уровня\n{} {} второго уровня\n'
                                           '{} {} третьего уровня\n{} {} четвертого уровня\n{} {} пятого уровня'
                                           .format(data['users'][username][1], self.string_1,
                                                   data['users'][username][2], self.string_2,
                                                   data['users'][username][3], self.string_3,
                                                   data['users'][username][4], self.string_4,
                                                   data['users'][username][5], self.string_5))


class No_username(QMessageBox):
    def __init__(self):
        super().__init__()
        self.msg = QMessageBox.information(self, '', 'Такого логина нет в системе')


class Yes_username(QMessageBox):
    def __init__(self):
        super().__init__()
        self.msg = QMessageBox.information(self, '', 'Такой логин есть в системе')


class Wrong_password(QMessageBox):
    def __init__(self):
        super().__init__()
        self.msg = QMessageBox.information(self, '', 'Неверный пароль')


class Sign_up(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация')
        self.resize(600, 300)
        # шрифт
        self.font = QFont()
        self.font.setPointSize(10)

        self.label_user = QLabel('USERNAME', self)
        self.label_user.setGeometry(160, 95, 81, 31)
        self.label_user.setFont(self.font)

        self.label_password = QLabel('PASSWORD', self)
        self.label_password.setGeometry(160, 145, 81, 31)
        self.label_password.setFont(self.font)

        self.user_line = QLineEdit(self)
        self.user_line.setGeometry(250, 100, 141, 20)
        self.password_line = QLineEdit(self)
        self.password_line.setGeometry(250, 150, 141, 20)

        self.signup_button = QPushButton('Sign Up', self)
        self.signup_button.setGeometry(280, 220, 75, 23)
        self.signup_button.setStyleSheet("QPushButton {background-color: rgb(30,144,225);"
                                         " color: White; border-radius: 8px;}"
                                         "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.signup_button.clicked.connect(self.registration)
        self.show()

    def yes_username(self):
        self.y_username = Yes_username()

    def registration(self):
        self.username_reg = self.user_line.text()
        self.password_reg = self.password_line.text()
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
            self.data = yaml.safe_load(file)
        if self.username_reg not in self.data['users']:
            self.data['users'][self.username_reg] = {'password': self.password_reg, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
            with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'w') as file:
                yaml.dump(self.data, file, default_flow_style=False)
            self.mainwindow = ShopWindow(self.username_reg, self.password_reg)
            self.close()
            self.mainwindow.show()
        else:
            self.yes_username()
            self.user_line.clear()
            self.password_line.clear()


class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход')
        self.resize(600, 300)
        # шрифт
        self.font = QFont()
        self.font.setPointSize(10)

        self.label_user_log = QLabel('USERNAME', self)
        self.label_user_log.setGeometry(160, 95, 81, 31)
        self.label_user_log.setFont(self.font)

        self.label_password_log = QLabel('PASSWORD', self)
        self.label_password_log.setGeometry(160, 145, 81, 31)
        self.label_password_log.setFont(self.font)

        self.user_line_log = QLineEdit(self)
        self.user_line_log.setGeometry(250, 100, 141, 20)
        self.password_line_log = QLineEdit(self)
        self.password_line_log.setGeometry(250, 150, 141, 20)

        self.login_button = QPushButton('Login', self)
        self.login_button.setGeometry(220, 220, 75, 23)
        self.login_button.setStyleSheet("QPushButton {background-color: rgb(30,144,225);"
                                        " color: White; border-radius: 8px;}"
                                        "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.login_button.clicked.connect(self.click_login)

        self.signup_button_log = QPushButton('Sign Up', self)
        self.signup_button_log.setGeometry(330, 220, 75, 23)
        self.signup_button_log.setStyleSheet("QPushButton {background-color: rgb(255,255,255);"
                                             " color: rgb(30,144,225); border-radius: 8px;}"
                                             "QPushButton:pressed {background-color:rgb(220,220,220) ; }")
        self.signup_button_log.clicked.connect(self.click_sign_up)

    def no_username(self):
        self.non_username = No_username()

    def wrong_password(self):
        self.incorrect_password = Wrong_password()

    def click_login(self):
        self.username = self.user_line_log.text()
        self.password = self.password_line_log.text()
        with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
            self.data = yaml.safe_load(file)
        if self.username not in self.data['users']:
            self.no_username()
            self.user_line_log.clear()
            self.password_line_log.clear()
        elif self.password != self.data['users'][self.username]['password']:
            self.wrong_password()
            self.password_line_log.clear()
        else:
            self.mainwindow = ShopWindow(self.username, self.password)
            self.close()
            self.mainwindow.show()

    def click_sign_up(self):
        self.sign_up = Sign_up()
        self.close()
        self.sign_up.show()
