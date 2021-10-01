from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import yaml

class ShopWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Бронирование товаров в магазине', self)
        self.label.setGeometry(10, -100, 300, 300)
        self.label.setText('другой текст')
        self.button = QPushButton('')
        self.resize(1000, 300)
