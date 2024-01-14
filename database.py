from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()

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

        query.exec("CREATE TABLE IF NOT EXISTS Participants (ID integer primary key AUTOINCREMENT, name VARCHAR(70), "
                   "Age INTEGER, Gender VARCHAR(10), Address VARCHAR(100), Phone VARCHAR(15), Email VARCHAR(50), "
                   "Event VARCHAR(50))")

        query.exec("CREATE TABLE IF NOT EXISTS Gallery (ID integer primary key AUTOINCREMENT, Photo BLOB,"
                   "Event INTEGER, FOREIGN KEY (Event) REFERENCES Events(ID))")

        return True