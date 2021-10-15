from PyQt5.QtWidgets import QApplication

from lib.window import Login
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())


