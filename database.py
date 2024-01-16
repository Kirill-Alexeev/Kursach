from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlQueryModel, QSqlQuery


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_database()

    def create_database(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('smartsity_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получается открыть базу данных",
                                           "Нажмите Закрыть для выхода", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS Events (ID integer primary key AUTOINCREMENT, Title VARCHAR(30), "
                   "Date VARCHAR(20), Participants INTEGER, Description VARCHAR(300), "
                   "FOREIGN KEY (Participants) REFERENCES Participants(ID))")

        query.exec("CREATE TABLE IF NOT EXISTS Participants (ID integer primary key AUTOINCREMENT, Name VARCHAR(70), "
                   "Age INTEGER, Gender VARCHAR(10), Address VARCHAR(100), Phone VARCHAR(15), Email VARCHAR(50), "
                   "Event VARCHAR(50))")

        query.exec("CREATE TABLE IF NOT EXISTS Gallery (ID integer primary key AUTOINCREMENT, Photo BLOB,"
                   "Event INTEGER, FOREIGN KEY (Event) REFERENCES Events(ID))")

        query.exec("SELECT * FROM Events")

        if not query.next():
            event_data = [
                ("Волейбол", "2022-09-14", 0, "Соревнования по волейболу среди мужчин и женщин"),
                ("Баскетбол", "2022-09-14", 0, "Турнир по баскетболу для молодёжи до 20 лет"),
                ("Футбол", "2022-10-15", 0, "Товарищеские матчи по футболу"),
                ("Настольный теннис", "2022-10-15", 0, "Соревнования по настольному теннису"),
                ("Шахматы", "2022-10-16", 0, "Турнир для всех желающих"),
                ("Забег", "2022-10-16", 0, "Дистанция длиной 10 километров. Для тех кто хочет бросить себе вызов"),
                ("Кулинарный фестиваль", "2022-10-16", 0, "Множество фургонов с различными гастрономическими шедеврами"),
                ("Выставочная композиция", "2022-10-17", 0, "Новейшие разработки, технологические прорывы года"),
                ("Стратегические сессии", "2022-10-17", 0, "Интереснейшие лекции на различные темы, возможность "
                                                           "пообщаться с видными деятелями культуры и бизнеса")
            ]

            for event in event_data:
                query.prepare("INSERT INTO Events (title, date, participants, description) VALUES (?, ?, ?, ?)")
                query.addBindValue(event[0])  # Название мероприятия
                query.addBindValue(event[1])  # Дата проведения
                query.addBindValue(event[2])  # Количество участников
                query.addBindValue(event[3])  # Описание
                if not query.exec():
                    print("Ошибка добавления события:", query.lastError().text())

        model = QSqlQueryModel()
        model.setQuery("SELECT title FROM Events", db)
        return model
