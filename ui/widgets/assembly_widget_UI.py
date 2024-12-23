# Form implementation generated from reading ui file 'C:\Users\Jared\Documents\Code\Python-Projects\Inventory Manager\ui\widgets\assembly_widget.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(945, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.assembly_widget = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assembly_widget.sizePolicy().hasHeightForWidth())
        self.assembly_widget.setSizePolicy(sizePolicy)
        self.assembly_widget.setObjectName("assembly_widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.assembly_widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_total_cost_for_assembly = QtWidgets.QLabel(parent=self.assembly_widget)
        self.label_total_cost_for_assembly.setWordWrap(True)
        self.label_total_cost_for_assembly.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_total_cost_for_assembly.setObjectName("label_total_cost_for_assembly")
        self.verticalLayout_14.addWidget(self.label_total_cost_for_assembly)
        self.verticalWidget_4 = QtWidgets.QWidget(parent=self.assembly_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy)
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalWidget_4)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.image_layout = QtWidgets.QVBoxLayout()
        self.image_layout.setObjectName("image_layout")
        self.verticalLayout_13.addLayout(self.image_layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_quantity = QtWidgets.QDoubleSpinBox(parent=self.verticalWidget_4)
        self.doubleSpinBox_quantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBox_quantity.setSpecialValueText("")
        self.doubleSpinBox_quantity.setDecimals(0)
        self.doubleSpinBox_quantity.setMaximum(999999999999999.0)
        self.doubleSpinBox_quantity.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.doubleSpinBox_quantity.setObjectName("doubleSpinBox_quantity")
        self.gridLayout.addWidget(self.doubleSpinBox_quantity, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalWidget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalWidget_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.expected_time_to_complete_layout = QtWidgets.QVBoxLayout()
        self.expected_time_to_complete_layout.setObjectName("expected_time_to_complete_layout")
        self.gridLayout.addLayout(self.expected_time_to_complete_layout, 1, 1, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout)
        self.flowtag_data_widget = QtWidgets.QWidget(parent=self.verticalWidget_4)
        self.flowtag_data_widget.setObjectName("flowtag_data_widget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.flowtag_data_widget)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.flowtag_data_layout = QtWidgets.QVBoxLayout()
        self.flowtag_data_layout.setObjectName("flowtag_data_layout")
        self.verticalLayout_17.addLayout(self.flowtag_data_layout)
        self.verticalLayout_13.addWidget(self.flowtag_data_widget)
        self.pushButton_show_parts_list_summary = QtWidgets.QPushButton(parent=self.verticalWidget_4)
        self.pushButton_show_parts_list_summary.setObjectName("pushButton_show_parts_list_summary")
        self.verticalLayout_13.addWidget(self.pushButton_show_parts_list_summary)
        self.horizontalLayout.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalWidget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.assembly_files_layout = QtWidgets.QHBoxLayout()
        self.assembly_files_layout.setObjectName("assembly_files_layout")
        self.verticalLayout_12.addLayout(self.assembly_files_layout)
        self.flowtag_widget_settings = QtWidgets.QWidget(parent=self.verticalWidget_4)
        self.flowtag_widget_settings.setObjectName("flowtag_widget_settings")
        self.formLayout_2 = QtWidgets.QFormLayout(self.flowtag_widget_settings)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(parent=self.flowtag_widget_settings)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.comboBox_assembly_flow_tag = QtWidgets.QComboBox(parent=self.flowtag_widget_settings)
        self.comboBox_assembly_flow_tag.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_assembly_flow_tag.setObjectName("comboBox_assembly_flow_tag")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.comboBox_assembly_flow_tag)
        self.paint_widget = QtWidgets.QWidget(parent=self.flowtag_widget_settings)
        self.paint_widget.setObjectName("paint_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.paint_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.paint_layout = QtWidgets.QHBoxLayout()
        self.paint_layout.setObjectName("paint_layout")
        self.verticalLayout_18.addLayout(self.paint_layout)
        self.verticalLayout.addLayout(self.verticalLayout_18)
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.paint_widget)
        self.checkBox_not_part_of_process = QtWidgets.QCheckBox(parent=self.flowtag_widget_settings)
        self.checkBox_not_part_of_process.setObjectName("checkBox_not_part_of_process")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBox_not_part_of_process)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.formLayout_3)
        self.verticalLayout_12.addWidget(self.flowtag_widget_settings)
        self.verticalLayout_12.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_12)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_14.addWidget(self.verticalWidget_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_laser_cut_parts = QtWidgets.QPushButton(parent=self.assembly_widget)
        self.pushButton_laser_cut_parts.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_laser_cut_parts.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_laser_cut_parts.setCheckable(True)
        self.pushButton_laser_cut_parts.setObjectName("pushButton_laser_cut_parts")
        self.verticalLayout_4.addWidget(self.pushButton_laser_cut_parts)
        self.laser_cut_widget = QtWidgets.QWidget(parent=self.assembly_widget)
        self.laser_cut_widget.setObjectName("laser_cut_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.laser_cut_widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.laser_cut_parts_layout = QtWidgets.QVBoxLayout()
        self.laser_cut_parts_layout.setObjectName("laser_cut_parts_layout")
        self.verticalLayout_5.addLayout(self.laser_cut_parts_layout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_laser_cut_part_button = QtWidgets.QPushButton(parent=self.laser_cut_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_laser_cut_part_button.sizePolicy().hasHeightForWidth())
        self.add_laser_cut_part_button.setSizePolicy(sizePolicy)
        self.add_laser_cut_part_button.setDefault(True)
        self.add_laser_cut_part_button.setObjectName("add_laser_cut_part_button")
        self.horizontalLayout_4.addWidget(self.add_laser_cut_part_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addWidget(self.laser_cut_widget)
        self.verticalLayout_14.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_components = QtWidgets.QPushButton(parent=self.assembly_widget)
        self.pushButton_components.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_components.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_components.setCheckable(True)
        self.pushButton_components.setObjectName("pushButton_components")
        self.verticalLayout_3.addWidget(self.pushButton_components)
        self.component_widget = QtWidgets.QWidget(parent=self.assembly_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.component_widget.sizePolicy().hasHeightForWidth())
        self.component_widget.setSizePolicy(sizePolicy)
        self.component_widget.setObjectName("component_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.component_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.components_layout = QtWidgets.QVBoxLayout()
        self.components_layout.setObjectName("components_layout")
        self.verticalLayout_6.addLayout(self.components_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_component_button = QtWidgets.QPushButton(parent=self.component_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_component_button.sizePolicy().hasHeightForWidth())
        self.add_component_button.setSizePolicy(sizePolicy)
        self.add_component_button.setDefault(True)
        self.add_component_button.setObjectName("add_component_button")
        self.horizontalLayout_3.addWidget(self.add_component_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addWidget(self.component_widget)
        self.verticalLayout_14.addLayout(self.verticalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_sub_assemblies = QtWidgets.QPushButton(parent=self.assembly_widget)
        self.pushButton_sub_assemblies.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_sub_assemblies.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_sub_assemblies.setCheckable(True)
        self.pushButton_sub_assemblies.setChecked(False)
        self.pushButton_sub_assemblies.setObjectName("pushButton_sub_assemblies")
        self.verticalLayout_10.addWidget(self.pushButton_sub_assemblies)
        self.sub_assemblies_widget = QtWidgets.QWidget(parent=self.assembly_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub_assemblies_widget.sizePolicy().hasHeightForWidth())
        self.sub_assemblies_widget.setSizePolicy(sizePolicy)
        self.sub_assemblies_widget.setObjectName("sub_assemblies_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.sub_assemblies_widget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.sub_assembly_layout = QtWidgets.QVBoxLayout()
        self.sub_assembly_layout.setContentsMargins(9, 9, 9, 9)
        self.sub_assembly_layout.setObjectName("sub_assembly_layout")
        self.verticalLayout_11.addLayout(self.sub_assembly_layout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(9, 0, 0, 9)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.add_new_sub_assembly_button = QtWidgets.QPushButton(parent=self.sub_assemblies_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_sub_assembly_button.sizePolicy().hasHeightForWidth())
        self.add_new_sub_assembly_button.setSizePolicy(sizePolicy)
        self.add_new_sub_assembly_button.setDefault(True)
        self.add_new_sub_assembly_button.setObjectName("add_new_sub_assembly_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.add_new_sub_assembly_button)
        self.add_existing_assembly_button = QtWidgets.QPushButton(parent=self.sub_assemblies_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_existing_assembly_button.sizePolicy().hasHeightForWidth())
        self.add_existing_assembly_button.setSizePolicy(sizePolicy)
        self.add_existing_assembly_button.setDefault(True)
        self.add_existing_assembly_button.setObjectName("add_existing_assembly_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.add_existing_assembly_button)
        self.verticalLayout_11.addLayout(self.formLayout)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_10.addWidget(self.sub_assemblies_widget)
        self.verticalLayout_14.addLayout(self.verticalLayout_10)
        self.verticalLayout_14.setStretch(4, 1)
        self.verticalLayout_9.addLayout(self.verticalLayout_14)
        self.verticalLayout_8.addWidget(self.assembly_widget)
        self.label_3.setBuddy(self.doubleSpinBox_quantity)
        self.label.setBuddy(self.comboBox_assembly_flow_tag)

        self.retranslateUi(Form)
        self.pushButton_laser_cut_parts.clicked['bool'].connect(self.laser_cut_widget.setVisible) # type: ignore
        self.pushButton_components.clicked['bool'].connect(self.component_widget.setVisible) # type: ignore
        self.pushButton_sub_assemblies.clicked['bool'].connect(self.sub_assemblies_widget.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_total_cost_for_assembly.setText(_translate("Form", "Total Cost for Assembly: $0.00"))
        self.doubleSpinBox_quantity.setToolTip(_translate("Form", "Quantity multiplier"))
        self.label_4.setText(_translate("Form", "Exp. Dur.:"))
        self.label_3.setText(_translate("Form", "Quantity:"))
        self.pushButton_show_parts_list_summary.setText(_translate("Form", "Show Parts List Summary"))
        self.label_2.setText(_translate("Form", "Assembly files:"))
        self.label.setText(_translate("Form", "Assembly flowtag:"))
        self.checkBox_not_part_of_process.setToolTip(_translate("Form", "Flow tags ignored as they’re irrelevant to the upper-level assembly"))
        self.checkBox_not_part_of_process.setText(_translate("Form", "Not part of the process"))
        self.pushButton_laser_cut_parts.setText(_translate("Form", "Laser Cut Parts"))
        self.add_laser_cut_part_button.setText(_translate("Form", "Add Laser Cut Part"))
        self.pushButton_components.setText(_translate("Form", "Components"))
        self.add_component_button.setText(_translate("Form", "Add Component"))
        self.pushButton_sub_assemblies.setText(_translate("Form", "Sub Assemblies"))
        self.add_new_sub_assembly_button.setText(_translate("Form", "Add New Sub Assembly"))
        self.add_existing_assembly_button.setText(_translate("Form", "Add Existing Assembly"))