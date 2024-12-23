# Form implementation generated from reading ui file 'C:\Users\Jared\Documents\Code\Python-Projects\Inventory Manager\ui\widgets\workspace_tab_widget.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 888)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_view_parts = QtWidgets.QPushButton(parent=Form)
        self.pushButton_view_parts.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_view_parts.sizePolicy().hasHeightForWidth())
        self.pushButton_view_parts.setSizePolicy(sizePolicy)
        self.pushButton_view_parts.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_view_parts.setFont(font)
        self.pushButton_view_parts.setCheckable(True)
        self.pushButton_view_parts.setChecked(True)
        self.pushButton_view_parts.setDefault(False)
        self.pushButton_view_parts.setFlat(True)
        self.pushButton_view_parts.setObjectName("pushButton_view_parts")
        self.horizontalLayout_3.addWidget(self.pushButton_view_parts)
        self.pushButton_view_assemblies = QtWidgets.QPushButton(parent=Form)
        self.pushButton_view_assemblies.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_view_assemblies.sizePolicy().hasHeightForWidth())
        self.pushButton_view_assemblies.setSizePolicy(sizePolicy)
        self.pushButton_view_assemblies.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_view_assemblies.setFont(font)
        self.pushButton_view_assemblies.setCheckable(True)
        self.pushButton_view_assemblies.setFlat(True)
        self.pushButton_view_assemblies.setObjectName("pushButton_view_assemblies")
        self.horizontalLayout_3.addWidget(self.pushButton_view_assemblies)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sort_layout = QtWidgets.QHBoxLayout()
        self.sort_layout.setObjectName("sort_layout")
        self.horizontalLayout.addLayout(self.sort_layout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_search = QtWidgets.QPushButton(parent=Form)
        self.pushButton_search.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_search.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_search.setStyleSheet("QPushButton#pushButton_search{\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}")
        self.pushButton_search.setText("")
        icon = QtGui.QIcon.fromTheme("edit-find")
        self.pushButton_search.setIcon(icon)
        self.pushButton_search.setFlat(True)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_4.addWidget(self.pushButton_search)
        self.lineEdit_search = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_search.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_search.setStyleSheet("QLineEdit#lineEdit_search{\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_4.addWidget(self.lineEdit_search)
        self.pushButton_clear_search = QtWidgets.QPushButton(parent=Form)
        self.pushButton_clear_search.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_clear_search.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_clear_search.setStyleSheet("QPushButton#pushButton_clear_search{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"}")
        self.pushButton_clear_search.setText("")
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.pushButton_clear_search.setIcon(icon)
        self.pushButton_clear_search.setFlat(True)
        self.pushButton_clear_search.setObjectName("pushButton_clear_search")
        self.horizontalLayout_4.addWidget(self.pushButton_clear_search)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.menu_buttons_layout = QtWidgets.QHBoxLayout()
        self.menu_buttons_layout.setObjectName("menu_buttons_layout")
        self.horizontalLayout.addLayout(self.menu_buttons_layout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.tags_layout = QtWidgets.QHBoxLayout()
        self.tags_layout.setSpacing(0)
        self.tags_layout.setObjectName("tags_layout")
        self.verticalLayout_2.addLayout(self.tags_layout)
        self.workspace_layout = QtWidgets.QVBoxLayout()
        self.workspace_layout.setSpacing(0)
        self.workspace_layout.setObjectName("workspace_layout")
        self.verticalLayout_2.addLayout(self.workspace_layout)
        self.verticalLayout_2.setStretch(6, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_view_parts.setText(_translate("Form", "View Parts"))
        self.pushButton_view_assemblies.setText(_translate("Form", "View Assemblies"))
        self.lineEdit_search.setToolTip(_translate("Form", "Use commas ( , ) to use multiple search queries."))
        self.lineEdit_search.setPlaceholderText(_translate("Form", "Search parts..."))