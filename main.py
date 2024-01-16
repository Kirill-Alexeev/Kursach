import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QModelIndex
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from main_window import Ui_MainWindow
from gallery import Ui_Dialog
from database import Data


class SmartCity(QMainWindow):
    def __init__(self):
        super(SmartCity, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.base = Data()

        self.model = self.base.create_database()
        self.ui.listView.setModel(self.model)
        self.ui.listView.clicked.connect(self.on_click)

        self.ui.pushButton.clicked.connect(self.open_gallery_window)
        self.ui.pushButton_2.clicked.connect(self.add_new_participants)

    def open_gallery_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def add_new_participants(self):
        name = self.ui.lineEdit.text()
        age = self.ui.lineEdit_2.text()
        gender = self.ui.lineEdit_3.text()
        address = self.ui.lineEdit_4.text()
        phone = self.ui.lineEdit_5.text()
        email = self.ui.lineEdit_6.text()
        event = self.ui.comboBox.currentText()

        query = QSqlQuery()
        query.prepare(
           "INSERT INTO Participants (Name, Age, Gender, Address, Phone, Email, Event) VALUES (?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(age)
        query.addBindValue(gender)
        query.addBindValue(address)
        query.addBindValue(phone)
        query.addBindValue(email)
        query.addBindValue(event)

        if query.exec():
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Заявка отправлена!")
            msg_box.setWindowTitle("Успешно")
            msg_box.setStandardButtons(QMessageBox.Ok)

            msg_box.exec()
        else:
            error_message = "Ошибка отправки заявки: " + query.lastError().text()
            QMessageBox.critical(self, 'Ошибка', error_message)

    def on_click(self, index: QModelIndex):
        title = index.data()
        query = QSqlQuery()
        query.prepare("SELECT * FROM Events WHERE title=:title")
        query.bindValue(":title", title)
        if query.exec():
            query.first()
            # Выводим информацию о мероприятии
            info_text = f"Название: {query.value('Title')}\nДата проведения: {query.value('Date')}\nКоличество участников: {query.value('Participants')}\nОписание: {query.value('Description')}"
            self.ui.label_27.setText(info_text)
        else:
            print("Ошибка запроса:", query.lastError().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmartCity()
    window.show()

    sys.exit(app.exec())
