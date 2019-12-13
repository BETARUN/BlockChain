from PyQt5 import QtCore, QtGui, QtWidgets

class BankUI(object):
    def setupUi(self, Bank):
        Bank.setObjectName("Bank")
        Bank.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(Bank)
        self.centralwidget.setObjectName("centralwidget")
        self.btnquit = QtWidgets.QPushButton(self.centralwidget)
        self.btnquit.setGeometry(QtCore.QRect(350, 20, 90, 25))
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(60, 90, 350, 150))
        Bank.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bank)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 20))
        self.menubar.setObjectName("menubar")
        Bank.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bank)
        self.statusbar.setObjectName("statusbar")
        Bank.setStatusBar(self.statusbar)
        self.retranslateUi(Bank)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(140, 50, 200, 30))
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.btnreject = QtWidgets.QPushButton(self.layoutWidget)
        self.btnreject.setObjectName("btnreject")
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_authorize = QtWidgets.QPushButton(self.layoutWidget)
        self.btnquit.setObjectName("btnquit")
        self.layoutWidget.setGeometry(QtCore.QRect(80, 260, 320, 20))
        self.btn_authorize.setObjectName("btn_authorize")
        self.horizontalLayout.addWidget(self.btn_authorize)
        self.prompt.setObjectName("prompt")
        self.horizontalLayout.addWidget(self.btnreject)
        QtCore.QMetaObject.connectSlotsByName(Bank)

    def retranslateUi(self, Bank):
        _translate = QtCore.QCoreApplication.translate
        Bank.setWindowTitle(_translate("Bank", "Window"))
        self.btnquit.setText(_translate("Bank", "Close"))
        self.btn_authorize.setText(_translate("Bank", "Authorize"))
        self.btnreject.setText(_translate("Bank", "Close"))
        self.prompt.setText(_translate("Bank", "click to select"))
