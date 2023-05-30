# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Code\Python-Projects\Inventory Manager\ui\generate_quote_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 295)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget#widget{\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"    border: 1px solid  #3daee9;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTitle = QtWidgets.QLabel(self.widget)
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border: 1px solid  #3daee9;\n"
"border-bottom: none;\n"
"")
        self.lblTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTitle.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_3.addWidget(self.lblTitle)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.iconHolder = QtWidgets.QVBoxLayout()
        self.iconHolder.setSpacing(0)
        self.iconHolder.setObjectName("iconHolder")
        self.verticalLayout_2.addLayout(self.iconHolder)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 434, 98))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblMessage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout_4.addWidget(self.lblMessage)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_quote = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quote.sizePolicy().hasHeightForWidth())
        self.pushButton_quote.setSizePolicy(sizePolicy)
        self.pushButton_quote.setMinimumSize(QtCore.QSize(220, 40))
        self.pushButton_quote.setStyleSheet("QPushButton#pushButton_quote{\n"
"    color: #ffffff;\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_quote:checked{\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"}\n"
"QPushButton#pushButton_quote:hover{\n"
"    background-color: #48b6ed;\n"
"    border-color: #48b6ed;\n"
"}\n"
"QPushButton#pushButton_quote:pressed{\n"
"    background-color: #2b92c5;\n"
"    border-color: #2b92c5;\n"
"}\n"
"\n"
"QPushButton#pushButton_quote:!checked {\n"
"    background-color: rgb(71, 71, 71);\n"
"    border: 0.01em solid rgb(76, 76, 76);\n"
"    border-radius: 5px;\n"
"    color: grey;\n"
"}\n"
"\n"
"QPushButton:hover#pushButton_quote:!checked {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: 0.01em solid rgb(71, 76, 88);\n"
"}\n"
"\n"
"QPushButton:pressed#pushButton_quote:!checked {\n"
"    background-color: rgb(39, 39, 39);\n"
"    border: 0.01em solid rgb(47, 50, 57);\n"
"}")
        self.pushButton_quote.setCheckable(True)
        self.pushButton_quote.setChecked(True)
        self.pushButton_quote.setObjectName("pushButton_quote")
        self.gridLayout.addWidget(self.pushButton_quote, 0, 0, 1, 1)
        self.pushButton_update_inventory = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update_inventory.sizePolicy().hasHeightForWidth())
        self.pushButton_update_inventory.setSizePolicy(sizePolicy)
        self.pushButton_update_inventory.setMinimumSize(QtCore.QSize(220, 39))
        self.pushButton_update_inventory.setAutoFillBackground(False)
        self.pushButton_update_inventory.setStyleSheet("QPushButton#pushButton_update_inventory{\n"
"    color: #ffffff;\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_update_inventory:checked{\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"}\n"
"QPushButton#pushButton_update_inventory:hover{\n"
"    background-color: #48b6ed;\n"
"    border-color: #48b6ed;\n"
"}\n"
"QPushButton#pushButton_update_inventory:pressed{\n"
"    background-color: #2b92c5;\n"
"    border-color: #2b92c5;\n"
"}\n"
"\n"
"QPushButton#pushButton_update_inventory:!checked {\n"
"    background-color: rgb(71, 71, 71);\n"
"    border: 0.01em solid rgb(76, 76, 76);\n"
"    border-radius: 5px;\n"
"    color: grey;\n"
"}\n"
"\n"
"QPushButton:hover#pushButton_update_inventory:!checked {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: 0.01em solid rgb(71, 76, 88);\n"
"}\n"
"\n"
"QPushButton:pressed#pushButton_update_inventory:!checked {\n"
"    background-color: rgb(39, 39, 39);\n"
"    border: 0.01em solid rgb(47, 50, 57);\n"
"}")
        self.pushButton_update_inventory.setCheckable(True)
        self.pushButton_update_inventory.setObjectName("pushButton_update_inventory")
        self.gridLayout.addWidget(self.pushButton_update_inventory, 2, 1, 1, 1)
        self.pushButton_workorder = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_workorder.sizePolicy().hasHeightForWidth())
        self.pushButton_workorder.setSizePolicy(sizePolicy)
        self.pushButton_workorder.setMinimumSize(QtCore.QSize(220, 40))
        self.pushButton_workorder.setStyleSheet("QPushButton#pushButton_workorder{\n"
"    color: #ffffff;\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_workorder:checked{\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"}\n"
"QPushButton#pushButton_workorder:hover{\n"
"    background-color: #48b6ed;\n"
"    border-color: #48b6ed;\n"
"}\n"
"QPushButton#pushButton_workorder:pressed{\n"
"    background-color: #2b92c5;\n"
"    border-color: #2b92c5;\n"
"}\n"
"\n"
"QPushButton#pushButton_workorder:!checked {\n"
"    background-color: rgb(71, 71, 71);\n"
"    border: 0.01em solid rgb(76, 76, 76);\n"
"    border-radius: 5px;\n"
"    color: grey;\n"
"}\n"
"\n"
"QPushButton:hover#pushButton_workorder:!checked {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: 0.01em solid rgb(71, 76, 88);\n"
"}\n"
"\n"
"QPushButton:pressed#pushButton_workorder:!checked {\n"
"    background-color: rgb(39, 39, 39);\n"
"    border: 0.01em solid rgb(47, 50, 57);\n"
"}")
        self.pushButton_workorder.setCheckable(True)
        self.pushButton_workorder.setObjectName("pushButton_workorder")
        self.gridLayout.addWidget(self.pushButton_workorder, 0, 1, 1, 1)
        self.pushButton_packingslip = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_packingslip.setMinimumSize(QtCore.QSize(220, 40))
        self.pushButton_packingslip.setStyleSheet("QPushButton#pushButton_packingslip{\n"
"    color: #ffffff;\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_packingslip:checked{\n"
"    background-color: #3daee9;\n"
"    border: 0.01em solid #3daee9;\n"
"}\n"
"QPushButton#pushButton_packingslip:hover{\n"
"    background-color: #48b6ed;\n"
"    border-color: #48b6ed;\n"
"}\n"
"QPushButton#pushButton_packingslip:pressed{\n"
"    background-color: #2b92c5;\n"
"    border-color: #2b92c5;\n"
"}\n"
"\n"
"QPushButton#pushButton_packingslip:!checked {\n"
"    background-color: rgb(71, 71, 71);\n"
"    border: 0.01em solid rgb(76, 76, 76);\n"
"    border-radius: 5px;\n"
"    color: grey;\n"
"}\n"
"\n"
"QPushButton:hover#pushButton_packingslip:!checked {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: 0.01em solid rgb(71, 76, 88);\n"
"}\n"
"\n"
"QPushButton:pressed#pushButton_packingslip:!checked {\n"
"    background-color: rgb(39, 39, 39);\n"
"    border: 0.01em solid rgb(47, 50, 57);\n"
"}")
        self.pushButton_packingslip.setCheckable(True)
        self.pushButton_packingslip.setObjectName("pushButton_packingslip")
        self.gridLayout.addWidget(self.pushButton_packingslip, 2, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.verticalLayout.addLayout(self.buttonsLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblTitle.setText(_translate("Form", "TextLabel"))
        self.lblMessage.setText(_translate("Form", "TextLabel"))
        self.groupBox.setTitle(_translate("Form", "Options"))
        self.pushButton_quote.setToolTip(_translate("Form", "Will generate and save a quote to the Quote directory"))
        self.pushButton_quote.setText(_translate("Form", "Generate Quote"))
        self.pushButton_update_inventory.setToolTip(_translate("Form", "Will add/update parts in inventory."))
        self.pushButton_update_inventory.setText(_translate("Form", "Do NOT Add Parts to Inventory"))
        self.pushButton_workorder.setToolTip(_translate("Form", "Will generate and save a workorder to the Workorder directory"))
        self.pushButton_workorder.setText(_translate("Form", "Do NOT Generate Workorder"))
        self.pushButton_packingslip.setText(_translate("Form", "Do NOT Generate Packing Slip"))
