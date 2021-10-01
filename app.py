from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = ShopWindow()
    window.show()
    app.exec()
   