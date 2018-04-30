import os
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import (QFile, QVariant, Qt)
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)

MAC = True
try:
    from PyQt5.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

ID, CATEGORY, SHORTDESC, LONGDESC = range(4)


class ReferenceDataDlg(QDialog):

    def __init__(self, parent=None):
        super(ReferenceDataDlg, self).__init__(parent)

        self.model = QSqlTableModel(self)
        self.model.setTable("reference")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, "ID")
        self.model.setHeaderData(CATEGORY, Qt.Horizontal,"小车编号")
        self.model.setHeaderData(SHORTDESC, Qt.Horizontal,"检查记录")
        self.model.setHeaderData(LONGDESC, Qt.Horizontal,"巡检日期")
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        buttonBox = QDialogButtonBox()
        addButton = buttonBox.addButton("&添加",
                QDialogButtonBox.ActionRole)
        deleteButton = buttonBox.addButton("&删除",
                QDialogButtonBox.ActionRole)
        sortButton = buttonBox.addButton("&排序",
                QDialogButtonBox.ActionRole)
        if not MAC:
            addButton.setFocusPolicy(Qt.NoFocus)
            deleteButton.setFocusPolicy(Qt.NoFocus)
            sortButton.setFocusPolicy(Qt.NoFocus)

        menu = QMenu(self)
        sortByCategoryAction = menu.addAction("按小车编号排序")
        sortByDescriptionAction = menu.addAction("按检查记录排序")
        sortByIDAction = menu.addAction("按编号顺序排序")
        sortButton.setMenu(menu)
        closeButton = buttonBox.addButton(QDialogButtonBox.Close)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

        addButton.clicked.connect(self.addRecord)
        deleteButton.clicked.connect(self.deleteRecord)
        sortByCategoryAction.triggered.connect(lambda:self.sort(CATEGORY))
        sortByDescriptionAction.triggered.connect(lambda:self.sort(SHORTDESC))
        sortByIDAction.triggered.connect(lambda:self.sort(ID))
        closeButton.clicked.connect(self.accept)
        self.setWindowTitle("巡检历史数据")
        self.setWindowIcon(QtGui.QIcon('icon/update_128px_1156069_easyicon.net.ico'))


    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, CATEGORY)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        category = record.value(CATEGORY)
        desc = record.value(SHORTDESC)
        if (QMessageBox.question(self, "Reference Data",
                ("确定删除 {1} 的数据?"
                .format(desc,category)),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()
        self.model.select()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()


def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "reference.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            "Database Error: {0}".format(db.lastError().text()))
        sys.exit(1)

    if create:
        query = QSqlQuery()
        query.exec_("""CREATE TABLE reference (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                category VARCHAR(30) NOT NULL,
                shortdesc VARCHAR(20) NOT NULL,
                longdesc VARCHAR(80))""")

    form = ReferenceDataDlg()
    form.show()
    sys.exit(app.exec_())

main()
