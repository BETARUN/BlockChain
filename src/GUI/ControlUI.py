from PyQt5 import QtCore, QtGui, QtWidgets

class ControlUI(object):
    def setupUi(self, ControlUI):
        ControlUI.setObjectName("ControlUI")
        ControlUI.resize(450, 400)
        self.centralwidget = QtWidgets.QWidget(ControlUI)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 80, 350, 250))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagereg = QtWidgets.QWidget()
        self.pagereg.setObjectName("pagereg")
        self.label = QtWidgets.QLabel(self.pagereg)
        self.label.setGeometry(QtCore.QRect(80, 20, 180, 30))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.pagereg)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 70, 250, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.edit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.edit_name.setObjectName("edit_name")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.labelname = QtWidgets.QLabel(self.layoutWidget)
        self.labelname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelname.setAlignment(QtCore.Qt.AlignCenter)
        self.labelname.setObjectName("labelname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name)
        self.labelpasswd = QtWidgets.QLabel(self.layoutWidget)
        self.labelpasswd.setObjectName("labelpasswd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelpasswd)
        self.editpasswd = QtWidgets.QLineEdit(self.layoutWidget)
        self.editpasswd.setObjectName("editpasswd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editpasswd)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelname)
        self.layoutWidget1 = QtWidgets.QWidget(self.pagereg)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 200, 200, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_register = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout.addWidget(self.btn_register)
        self.btn_reset = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.stackedWidget.addWidget(self.pagereg)
        self.pageinfo = QtWidgets.QWidget()
        self.pageinfo.setObjectName("pageinfo")
        self.textinfo = QtWidgets.QLabel(self.pageinfo)
        self.textinfo.setGeometry(QtCore.QRect(60, 0, 230, 50))
        self.textinfo.setObjectName("textinfo")
        self.table = QtWidgets.QTableWidget(self.pageinfo)
        self.table.setGeometry(QtCore.QRect(20, 40, 300, 200))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.pageinfo)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 30, 330, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.statusbar = QtWidgets.QStatusBar(ControlUI)
        self.statusbar.setObjectName("statusbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_select_register = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_select_register.setObjectName("btn_select_register")
        self.horizontalLayout_2.addWidget(self.btn_select_register)
        self.btnselectlist = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnselectlist.setObjectName("btnselectlist")
        self.horizontalLayout_2.addWidget(self.btnselectlist)
        self.btnquit = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnquit.setObjectName("btnquit")
        self.horizontalLayout_2.addWidget(self.btnquit)
        ControlUI.setCentralWidget(self.centralwidget)
        ControlUI.setStatusBar(self.statusbar)

        self.retranslateUi(ControlUI)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ControlUI)

    def retranslateUi(self, ControlUI):
        _translate = QtCore.QCoreApplication.translate
        ControlUI.setWindowTitle(_translate("ControlUI", "Window"))
        self.label.setText(_translate("ControlUI", "Register New Company"))
        self.labelpasswd.setText(_translate("ControlUI", "Password"))
        self.labelname.setText(_translate("ControlUI", "User"))
        self.btn_reset.setText(_translate("ControlUI", "Reset"))
        self.textinfo.setText(_translate("ControlUI", "Info"))
        self.btn_register.setText(_translate("ControlUI", "Register"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("ControlUI", "User"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("ControlUI", "Type"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("ControlUI", "Address"))
        self.btnselectlist.setText(_translate("ControlUI", "List"))
        self.btn_select_register.setText(_translate("ControlUI", "Register"))
        self.btnquit.setText(_translate("ControlUI", "Close"))
