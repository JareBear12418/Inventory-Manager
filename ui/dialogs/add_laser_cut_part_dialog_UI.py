# Form implementation generated from reading ui file 'c:\Users\Jared\Documents\Code\Python-Projects\Inventory Manager\ui\dialogs\add_laser_cut_part_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 626)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMessage = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_name.setClearButtonEnabled(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_4.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget_laser_cut_parts = QtWidgets.QListWidget(parent=self.widget)
        self.listWidget_laser_cut_parts.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget_laser_cut_parts.setObjectName("listWidget_laser_cut_parts")
        self.verticalLayout.addWidget(self.listWidget_laser_cut_parts)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.spinBox_current_quantity = QtWidgets.QDoubleSpinBox(parent=self.widget)
        self.spinBox_current_quantity.setMaximum(999999999.0)
        self.spinBox_current_quantity.setObjectName("spinBox_current_quantity")
        self.horizontalLayout_3.addWidget(self.spinBox_current_quantity)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_laser_cut_part_status = QtWidgets.QLabel(parent=self.widget)
        self.label_laser_cut_part_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_laser_cut_part_status.setObjectName("label_laser_cut_part_status")
        self.verticalLayout.addWidget(self.label_laser_cut_part_status)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.buttonsLayout.addItem(spacerItem)
        self.pushButton_add = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_add.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_add.setObjectName("pushButton_add")
        self.buttonsLayout.addWidget(self.pushButton_add)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.buttonsLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.buttonsLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)
        self.label.setBuddy(self.listWidget_laser_cut_parts)
        self.label_7.setBuddy(self.spinBox_current_quantity)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.spinBox_current_quantity, self.pushButton_add)
        Form.setTabOrder(self.pushButton_add, self.pushButton_cancel)
        Form.setTabOrder(self.pushButton_cancel, self.listWidget_laser_cut_parts)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblMessage.setText(_translate("Form", "Press 'Tab' to autofill.\n" "\n" "Press 'Add' when finished."))
        self.label_3.setText(_translate("Form", "Laser Cut Part Name:"))
        self.lineEdit_name.setPlaceholderText(_translate("Form", "Part name..."))
        self.label.setText(_translate("Form", "All Laser Cut Parts in Inventory:"))
        self.label_7.setText(_translate("Form", "Quantity:"))
        self.label_laser_cut_part_status.setText(_translate("Form", " * Laser Cut Part does NOT exist in inventory."))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
