import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow


class SmartCity(QMainWindow):
    def __init__(self):
        super(SmartCity, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmartCity()
    window.show()

    sys.exit(app.exec())
