from PyQt5.QtWidgets import QApplication, QMainWindow
from lib.window import ShopWindow

if __name__ == '__main__':
    app = QApplication([])
    window = ShopWindow()
    window.show()
    app.exec()
