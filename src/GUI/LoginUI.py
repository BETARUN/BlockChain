from PyQt5 import QtCore, QtGui, QtWidgets

class LoginUI(object):
    def setupUi(self, LoginUI):
        LoginUI.setObjectName("LoginUI")
        LoginUI.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(LoginUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 60, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 100, 200, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label2 = QtWidgets.QLabel(self.layoutWidget)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.layoutWidget)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.lineaccount = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineaccount.setObjectName("lineaccount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineaccount)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.line_pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_pwd.setObjectName("line_pwd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_pwd)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 200, 200, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.btnquit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnquit.setObjectName("btnquit")
        self.horizontalLayout.addWidget(self.btnquit)
        self.btnenter = QtWidgets.QPushButton(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnenter.setObjectName("btnenter")
        self.horizontalLayout.addWidget(self.btnenter)
        self.statusbar = QtWidgets.QStatusBar(LoginUI)
        self.statusbar.setObjectName("statusbar")
        LoginUI.setStatusBar(self.statusbar)
        LoginUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 20))
        self.menubar.setObjectName("menubar")
        LoginUI.setMenuBar(self.menubar)
        self.retranslateUi(LoginUI)
        self.btnquit.clicked.connect(LoginUI.close)
        QtCore.QMetaObject.connectSlotsByName(LoginUI)

    def retranslateUi(self, LoginUI):
        _translate = QtCore.QCoreApplication.translate
        LoginUI.setWindowTitle(_translate("LoginUI", "Window"))
        self.label.setText(_translate("LoginUI", "LogIn"))
        self.label2.setText(_translate("LoginUI", "User"))
        self.label3.setText(_translate("LoginUI", "Password"))
        self.btnquit.setText(_translate("LoginUI", "Close"))
        self.btnenter.setText(_translate("LoginUI", "Enter"))
