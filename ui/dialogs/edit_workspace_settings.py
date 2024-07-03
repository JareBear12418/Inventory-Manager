import contextlib
import copy
from functools import partial

from PyQt6 import uic
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction, QCursor, QIcon
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QWidget,
)

from ui.custom_widgets import AssemblyMultiToolBox, DeletePushButton
from utils.workspace.flow_tag import FlowTag, Group
from utils.workspace.flow_tags import FlowTags
from utils.workspace.status import Status
from utils.workspace.tag import Tag
from utils.workspace.workspace_settings import WorkspaceSettings


class TagWidget(QWidget):
    tagDeleted = pyqtSignal()

    def __init__(
        self,
        tag: Tag,
        remaining_tags: list[Tag],
        workspace_settings: WorkspaceSettings,
        parent: "FlowTagWidget",
    ):
        super().__init__(parent)
        self.parent = parent
        self.remaining_tags = remaining_tags
        self.workspace_settings = workspace_settings
        self.tag = tag
        self.setStyleSheet(
            "QWidget#tag_idget{border: 1px solid rgba(120, 120, 120, 70);}"
        )
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.tag_combobox = QComboBox(self)
        self.tag_combobox.addItems([tag.name for tag in self.remaining_tags])
        self.tag_combobox.setCurrentText(tag.name)
        self.tag_combobox.currentTextChanged.connect(self.tag_changed)
        self.tag_combobox.wheelEvent = lambda event: None
        self.arrow_label = QLabel("➜", self)
        self.delete_button = DeletePushButton(
            self, "Delete this tag", icon=QIcon("icons/trash.png")
        )
        self.delete_button.setFixedWidth(40)
        self.delete_button.clicked.connect(self.delete_tag)
        layout.addWidget(self.tag_combobox)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.arrow_label)
        self.setLayout(layout)

    def tag_changed(self):
        self.parent.tag_changed(self, self.tag, self.tag_combobox.currentText())

    def update_tag_selections(self, used_tags: list[str]):
        self.tag_combobox.blockSignals(True)
        self.tag_combobox.clear()
        self.tag_combobox.addItems(
            [
                tag.name
                for tag in self.workspace_settings.tags
                if tag.name not in used_tags
            ]
        )
        self.tag_combobox.addItem(self.tag.name)
        self.tag_combobox.setCurrentText(self.tag.name)
        self.tag_combobox.blockSignals(False)

    def delete_tag(self):
        self.tagDeleted.emit()
        self.deleteLater()


class FlowTagWidget(QWidget):
    def __init__(
        self, flow_tag: FlowTag, workspace_settings: WorkspaceSettings, parent: QWidget
    ):
        super().__init__(parent)
        self.parent = parent
        self.flow_tag = flow_tag
        self.workspace_settings = workspace_settings

        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.tag_layout = QHBoxLayout()
        self.tag_layout.setSpacing(0)
        self.tag_layout.setContentsMargins(0, 0, 0, 0)
        self.tag_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.add_tag_button = QPushButton("Add", self)
        self.add_tag_button.setFixedWidth(70)
        self.add_tag_button.clicked.connect(self.add_tag)

        layout.addLayout(self.tag_layout)
        layout.addWidget(self.add_tag_button)

        self.remaining_tags: list[Tag] = copy.copy(self.workspace_settings.tags)

        self.tag_widgets: list[TagWidget] = []
        self.setLayout(layout)
        self.update_tag_selections()
        self.load_data()

    def load_data(self):
        for tag in self.flow_tag.tags:
            tag_widget = TagWidget(
                tag, self.remaining_tags, self.workspace_settings, self
            )
            tag_widget.tagDeleted.connect(partial(self.delete_tag, tag_widget))
            self.tag_widgets.append(tag_widget)
            self.tag_layout.addWidget(tag_widget)
        self.update_tag_selections()

    def add_tag(self):
        new_tag = self.remaining_tags[0]
        tag_widget = TagWidget(
            new_tag, self.remaining_tags, self.workspace_settings, self
        )
        self.flow_tag.add_tag(new_tag)
        tag_widget.tagDeleted.connect(partial(self.delete_tag, tag_widget))
        self.tag_widgets.append(tag_widget)
        self.tag_layout.addWidget(tag_widget)
        self.remaining_tags.remove(new_tag)
        self.update_tag_selections()

    def delete_tag(self, deleted_tag_widget: TagWidget):
        self.tag_widgets.remove(deleted_tag_widget)
        self.flow_tag.remove_tag(deleted_tag_widget.tag)
        self.remaining_tags.append(deleted_tag_widget.tag)

        self.update_tag_selections()

    def tag_changed(self, tag_widget: TagWidget, old_tag: Tag, new_tag_name: str):
        index = self.flow_tag.tags.index(old_tag)
        self.flow_tag.tags.pop(index)
        tag = self.workspace_settings.get_tag(new_tag_name)
        self.flow_tag.tags.insert(index, tag)
        tag_widget.tag = tag
        self.update_tag_selections()

    def update_tag_selections(self):
        self.add_tag_button.setEnabled(
            len(self.flow_tag.tags) != len(self.workspace_settings.tags)
        )
        self.remaining_tags = [
            tag
            for tag in self.workspace_settings.tags
            if tag.name not in self.flow_tag.to_list()
        ]
        for tag_widget in self.tag_widgets:
            tag_widget.update_tag_selections(used_tags=self.flow_tag.to_list())


class FlowTagsTableWidget(QTableWidget):
    def __init__(
        self,
        flow_tag_group: FlowTags,
        workspace_settings: WorkspaceSettings,
        parent: QWidget,
    ):
        super().__init__(parent)
        self.flow_tag_group = flow_tag_group
        self.workspace_settings = workspace_settings
        self.table_items: dict[FlowTag, QTableWidgetItem] = {}
        self.flow_tag_counter: int = 0

        self.table_widgets: dict[
            FlowTag, dict[str, QTableWidgetItem | FlowTagWidget]
        ] = {}

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Name", "Flow Tag"])
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 600)
        self.horizontalHeader().setStretchLastSection(True)

        self.insertRow(0)
        self.setCellWidget(0, 0, self.create_button())
        if self.contextMenuPolicy() != Qt.ContextMenuPolicy.CustomContextMenu:
            self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            menu = QMenu(self)
            action = QAction(self)
            action.triggered.connect(self.delete_selected_flow_tags)
            action.setText("Delete selected flow tags")
            menu.addAction(action)
            self.customContextMenuRequested.connect(partial(self.open_group_menu, menu))
        self.load_data()
        self.cellChanged.connect(self.table_changed)

    def create_button(self) -> QPushButton:
        button = QPushButton("Create New Flow Tag", self)
        button.setFixedWidth(150)
        button.clicked.connect(self.add_flow_tag)
        return button

    def add_flow_tag(self):
        row_count = self.rowCount()

        if row_count > 0:
            self.removeCellWidget(row_count - 1, 0)

        self.insertRow(self.rowCount())
        flow_tag = FlowTag(
            f"FlowTag{self.flow_tag_counter}", [], self.workspace_settings
        )

        self.flow_tag_group.add_flow_tag(flow_tag)

        self.table_widgets.update({flow_tag: {}})

        table_item_name = QTableWidgetItem(flow_tag.name)
        self.setItem(row_count - 1, 0, table_item_name)
        self.table_widgets[flow_tag].update({"name": table_item_name})

        flow_tag_widget = FlowTagWidget(flow_tag, self.workspace_settings, self)
        self.setCellWidget(row_count - 1, 1, flow_tag_widget)
        self.table_widgets[flow_tag].update({"widget": flow_tag_widget})

        self.setRowHeight(row_count - 1, 50)

        self.setCellWidget(row_count, 0, self.create_button())
        self.setFixedHeight((self.rowCount() * 45) + 70)
        self.flow_tag_counter += 1

    def load_data(self):
        if self.rowCount() == 1:
            self.removeCellWidget(1, 0)

        for row, flow_tag in enumerate(self.flow_tag_group):
            self.insertRow(row)

            self.table_widgets.update({flow_tag: {}})

            table_item_name = QTableWidgetItem(flow_tag.name)
            self.setItem(row, 0, table_item_name)
            self.table_widgets[flow_tag].update({"name": table_item_name})

            flow_tag_widget = FlowTagWidget(flow_tag, self.workspace_settings, self)
            self.setCellWidget(row, 1, flow_tag_widget)
            self.table_widgets[flow_tag].update({"widget": flow_tag_widget})

            self.setRowHeight(row, 50)

        self.setFixedHeight((self.rowCount() * 45) + 70)
        self.flow_tag_counter = self.rowCount() - 1

    def add_tag(self, flow_tag: FlowTag):
        self.table_widgets[flow_tag]["widget"].add_tag()

    def delete_selected_flow_tags(self, flow_tag: FlowTag):
        if selected_flow_tags := self.get_selected_flow_tags():
            for flow_tag in selected_flow_tags:
                self.table_widgets[flow_tag]["widget"].deleteLater()
                self.removeRow(self.table_widgets[flow_tag]["name"].row())
                del self.table_widgets[flow_tag]
                self.flow_tag_group.remove_flow_tag(flow_tag)

    def get_selected_flow_tags(self) -> list[FlowTags]:
        selected_flow_tags: list[FlowTags] = []
        selected_flow_tags.extend(
            flow_tag
            for flow_tag, table_items in self.table_widgets.items()
            if table_items["name"].isSelected()
        )
        return selected_flow_tags

    def get_selected_flow_tag(self) -> FlowTag:
        for flow_tag, flow_tag_items in self.table_widgets.items():
            if flow_tag_items["name"].isSelected():
                return flow_tag

    def table_changed(self):
        self.blockSignals(True)
        with contextlib.suppress(KeyError):
            for flow_tag, table_item in self.table_widgets.items():
                flow_tag.name = table_item["name"].text()
        self.blockSignals(False)

    def open_group_menu(self, menu: QMenu) -> None:
        menu.exec(QCursor.pos())


class EditWorkspaceSettings(QDialog):
    def __init__(
        self,
        workspace_settings: WorkspaceSettings,
        parent=None,
    ) -> None:
        super().__init__(parent)
        uic.loadUi("ui/dialogs/edit_workspace_settings.ui", self)

        self.workspace_settings = workspace_settings

        self.assembly_groups_multi_tool_box = AssemblyMultiToolBox(self)
        self.laser_cut_parts_groups_multi_tool_box = AssemblyMultiToolBox(self)
        self.components_groups_multi_tool_box = AssemblyMultiToolBox(self)

        self.actve_groups_multi_tool_box: AssemblyMultiToolBox = (
            self.laser_cut_parts_groups_multi_tool_box
        )

        self.tabWidget = self.findChild(QTabWidget, "tabWidget")
        self.tabWidget.currentChanged.connect(self.tab_changed)

        self.flow_tag_tables: dict[FlowTags, FlowTagsTableWidget] = {}

        self.listWidget_select_tag = self.findChild(
            QListWidget, "listWidget_select_tag"
        )
        self.listWidget_select_tag.currentItemChanged.connect(
            self.tag_selection_changed
        )
        self.listWidget_select_tag.itemDoubleClicked.connect(self.rename_tag)
        self.last_selected_row = 0

        self.textEdit_notes = self.findChild(QTextEdit, "textEdit_notes")
        self.textEdit_notes.textChanged.connect(self.notes_changed)
        self.textEdit_notes.setText(self.workspace_settings.notes)

        self.groupBox_4 = self.findChild(QGroupBox, "groupBox_4")
        self.tableWidget_statuses = self.findChild(QTableWidget, "tableWidget_statuses")
        self.tableWidget_statuses.cellChanged.connect(self.status_table_changed)
        self.tableWidget_statuses.setColumnWidth(0, 300)
        self.tableWidget_statuses.setColumnWidth(1, 200)
        self.tableWidget_statuses.setColumnWidth(2, 200)
        self.tableWidget_statuses.setColumnWidth(3, 40)
        self.status_table_items: dict[
            Status, dict[str, QTableWidgetItem | QCheckBox]
        ] = {}
        self.pushButton_add_status.clicked.connect(self.add_status)

        self.groupBox_5 = self.findChild(QGroupBox, "groupBox_5")
        self.checkBox_enable_timer = self.findChild(QCheckBox, "checkBox_enable_timer")
        self.checkBox_enable_timer.checkStateChanged.connect(
            self.checkbox_enable_timer_changed
        )
        self.checkBox_show_all_items = self.findChild(
            QCheckBox, "checkBox_show_all_items"
        )
        self.checkBox_show_all_items.checkStateChanged.connect(
            self.checkbox_show_all_items_changed
        )
        self.plainTextEdit_next_flow_tag_message = self.findChild(
            QPlainTextEdit, "plainTextEdit_next_flow_tag_message"
        )
        self.plainTextEdit_next_flow_tag_message.textChanged.connect(
            self.next_flow_tag_message_changed
        )

        self.pushButton_add_tag.clicked.connect(self.add_tag)
        self.pushButton_delete_tag.clicked.connect(self.delete_tag)

        self.pushButton_create_new_assembly_group.clicked.connect(self.create_group)
        self.pushButton_create_new_laser_cut_part_group.clicked.connect(
            self.create_group
        )
        self.pushButton_create_new_components_group.clicked.connect(self.create_group)

        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_save_and_close.clicked.connect(self.save_and_close)
        self.pushButton_cancel.clicked.connect(self.reject)

        self.setWindowTitle("Edit Workspace Flow Tags")
        self.setWindowIcon(QIcon("icons/icon.png"))

        self.load_flow_tag_table_widgets()
        self.load_tags()
        self.showMaximized()

    def tab_changed(self):
        if self.tabWidget.currentIndex() == 0:
            self.actve_groups_multi_tool_box = self.assembly_groups_multi_tool_box
        elif self.tabWidget.currentIndex() == 1:
            self.actve_groups_multi_tool_box = (
                self.laser_cut_parts_groups_multi_tool_box
            )
        elif self.tabWidget.currentIndex() == 2:
            self.actve_groups_multi_tool_box = self.components_groups_multi_tool_box

    def create_group(self):
        name, ok = QInputDialog.getText(self, "Group name", "Enter a group name:")
        if name and ok:
            flow_tag_group = self.workspace_settings.create_group(name)
            if self.tabWidget.currentIndex() == 0:
                flow_tag_group.group = Group.ASSEMBLY
            elif self.tabWidget.currentIndex() == 1:
                flow_tag_group.group = Group.LASER_CUT_PART
            elif self.tabWidget.currentIndex() == 2:
                flow_tag_group.group = Group.COMPONENT
            self.add_group(flow_tag_group)

    def add_group(self, flow_tag_group: FlowTags):
        table_widget = FlowTagsTableWidget(
            flow_tag_group, self.workspace_settings, self
        )
        if flow_tag_group.group == Group.ASSEMBLY:
            self.assembly_groups_multi_tool_box.addItem(
                table_widget, flow_tag_group.name
            )
            delete_button = self.assembly_groups_multi_tool_box.getLastDeleteButton()
            delete_button.clicked.connect(partial(self.delete_group, flow_tag_group))
            input_box = self.assembly_groups_multi_tool_box.getLastInputBox()
            input_box.textChanged.connect(
                partial(self.rename_group, flow_tag_group, input_box)
            )
            duplicate_button = (
                self.assembly_groups_multi_tool_box.getLastDuplicateButton()
            )
            duplicate_button.clicked.connect(
                partial(self.duplicate_group, flow_tag_group)
            )
        elif flow_tag_group.group == Group.LASER_CUT_PART:
            self.laser_cut_parts_groups_multi_tool_box.addItem(
                table_widget, flow_tag_group.name
            )
            delete_button = (
                self.laser_cut_parts_groups_multi_tool_box.getLastDeleteButton()
            )
            delete_button.clicked.connect(partial(self.delete_group, flow_tag_group))
            input_box = self.laser_cut_parts_groups_multi_tool_box.getLastInputBox()
            input_box.textChanged.connect(
                partial(self.rename_group, flow_tag_group, input_box)
            )
            duplicate_button = (
                self.laser_cut_parts_groups_multi_tool_box.getLastDuplicateButton()
            )
            duplicate_button.clicked.connect(
                partial(self.duplicate_group, flow_tag_group)
            )
        elif flow_tag_group.group == Group.COMPONENT:
            self.components_groups_multi_tool_box.addItem(
                table_widget, flow_tag_group.name
            )
            delete_button = self.components_groups_multi_tool_box.getLastDeleteButton()
            delete_button.clicked.connect(partial(self.delete_group, flow_tag_group))
            input_box = self.components_groups_multi_tool_box.getLastInputBox()
            input_box.textChanged.connect(
                partial(self.rename_group, flow_tag_group, input_box)
            )
            duplicate_button = (
                self.components_groups_multi_tool_box.getLastDuplicateButton()
            )
            duplicate_button.clicked.connect(
                partial(self.duplicate_group, flow_tag_group)
            )
        self.flow_tag_tables.update({flow_tag_group: table_widget})

    def rename_group(self, flow_tag_group: FlowTags, input_box: QLineEdit):
        flow_tag_group.name = input_box.text()

    def delete_group(self, flow_tag_group: FlowTags):
        self.clear_layout(self.flow_tag_tables[flow_tag_group])
        if flow_tag_group.group == Group.ASSEMBLY:
            self.assembly_groups_multi_tool_box.removeItem(
                self.actve_groups_multi_tool_box.getWidget(
                    self.workspace_settings.flow_tags_group.index(flow_tag_group)
                )
            )
        elif flow_tag_group.group == Group.LASER_CUT_PART:
            self.laser_cut_parts_groups_multi_tool_box.removeItem(
                self.actve_groups_multi_tool_box.getWidget(
                    self.workspace_settings.flow_tags_group.index(flow_tag_group)
                )
            )
        elif flow_tag_group.group == Group.COMPONENT:
            self.components_groups_multi_tool_box.removeItem(
                self.actve_groups_multi_tool_box.getWidget(
                    self.workspace_settings.flow_tags_group.index(flow_tag_group)
                )
            )
        self.workspace_settings.delete_group(flow_tag_group)
        del self.flow_tag_tables[flow_tag_group]

    def duplicate_group(self, flow_tag_group: FlowTags):
        new_group = self.workspace_settings.create_group(
            f"{flow_tag_group.name} - Copy"
        )
        if self.tabWidget.currentIndex() == 0:
            new_group.group = Group.ASSEMBLY
        elif self.tabWidget.currentIndex() == 1:
            new_group.group = Group.LASER_CUT_PART
        elif self.tabWidget.currentIndex() == 2:
            new_group.group = Group.COMPONENT
        for flow_tag in flow_tag_group:
            new_group.add_flow_tag(flow_tag)
        self.add_group(new_group)

    def load_flow_tag_table_widgets(self):
        self.clear_layout(self.assemblies_flow_tag_layout)
        self.clear_layout(self.laser_cut_parts_flow_tag_layout)
        self.clear_layout(self.components_flow_tag_layout)
        self.assemblies_flow_tag_layout.addWidget(self.assembly_groups_multi_tool_box)
        self.laser_cut_parts_flow_tag_layout.addWidget(
            self.laser_cut_parts_groups_multi_tool_box
        )
        self.components_flow_tag_layout.addWidget(self.components_groups_multi_tool_box)
        for flow_tag_group in self.workspace_settings.flow_tags_group:
            self.add_group(flow_tag_group)

    def add_tag(self):
        tag_name, ok = QInputDialog.getText(self, "Add tag", "Enter a tag name:")
        if tag_name and ok:
            self.workspace_settings.create_tag(tag_name)
            self.load_tags()

    def delete_tag(self):
        tag_name, ok = QInputDialog.getItem(
            self,
            "Delete tag",
            "Select a tag to delete",
            self.workspace_settings.get_all_tags(),
            self.workspace_settings.get_all_tags().index(self.get_selected_tag().name),
            False,
        )
        if tag_name and ok:
            tag = self.workspace_settings.get_tag(tag_name)
            self.workspace_settings.remove_tag(tag)
            self.load_tags()

    def load_tags(self):
        self.listWidget_select_tag.blockSignals(True)
        self.listWidget_select_tag.clear()
        self.listWidget_select_tag.addItems(self.workspace_settings.get_all_tags())
        self.listWidget_select_tag.blockSignals(False)
        self.listWidget_select_tag.setCurrentRow(self.last_selected_row)
        self.update_tag_comboboxes()

    def update_tag_comboboxes(self):
        for flow_tag_table_widget in self.flow_tag_tables.values():
            for table_items in flow_tag_table_widget.table_widgets.values():
                widget: FlowTagWidget = table_items["widget"]
                widget.update_tag_selections()

    def rename_tag(self):
        current_tag = self.workspace_settings.get_tag(
            self.listWidget_select_tag.currentItem().text()
        )
        new_name, ok = QInputDialog.getText(
            self,
            "Rename tag",
            "Enter a new name for the selected tag:",
            text=current_tag.name,
        )
        if new_name and ok:
            if new_name in ["Staging", "Planning", "Editing"]:
                msg = QMessageBox(self)
                msg.setWindowTitle("Invalid name")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText(f"{new_name} cannot be used as a tag.")
                msg.exec()
                return
            current_tag.name = new_name
        self.load_tags()

    def get_selected_tag(self) -> Tag:
        if item := self.listWidget_select_tag.currentItem():
            if tag := item.text():
                return self.workspace_settings.get_tag(tag)

    def tag_selection_changed(self):
        self.last_selected_row = self.listWidget_select_tag.currentRow()
        self.load_status_table()
        self.load_attributes()

    def load_status_table(self):
        if selected_tag := self.get_selected_tag():
            self.groupBox_4.setTitle(f"Statuses for {selected_tag.name}")
            self.tableWidget_statuses.blockSignals(True)
            self.status_table_items.clear()
            self.tableWidget_statuses.clearContents()
            self.tableWidget_statuses.setRowCount(0)
            for row, status in enumerate(selected_tag.statuses):
                self.tableWidget_statuses.insertRow(row)
                self.status_table_items.update({status: {}})
                status_name = QTableWidgetItem(status.name)
                self.tableWidget_statuses.setItem(row, 0, status_name)
                self.status_table_items[status].update({"name": status_name})

                checkbox_moves_tag_forward = QCheckBox("Moves Tag Forward", self)
                checkbox_moves_tag_forward.setChecked(status.completed)
                checkbox_moves_tag_forward.stateChanged.connect(
                    partial(
                        self.checkbox_move_tag_forward_changed,
                        checkbox_moves_tag_forward,
                    )
                )
                self.tableWidget_statuses.setCellWidget(
                    row, 1, checkbox_moves_tag_forward
                )
                self.status_table_items[status].update(
                    {"checkbox_move_tag_forward": checkbox_moves_tag_forward}
                )

                checkbox_starts_timer = QCheckBox("Starts Timer", self)
                checkbox_starts_timer.setChecked(status.start_timer)
                checkbox_starts_timer.stateChanged.connect(self.status_table_changed)
                self.tableWidget_statuses.setCellWidget(row, 2, checkbox_starts_timer)
                self.status_table_items[status].update(
                    {"checkbox_starts_timer": checkbox_starts_timer}
                )

                def delete_status(status_to_delete: Status):
                    selected_tag.delete_status(status_to_delete)
                    self.load_status_table()

                delete_status_button = DeletePushButton(
                    self, "Delete status", QIcon("icons/trash.png")
                )
                delete_status_button.setFixedWidth(40)
                delete_status_button.clicked.connect(partial(delete_status, status))
                self.tableWidget_statuses.setCellWidget(row, 3, delete_status_button)

            self.tableWidget_statuses.blockSignals(False)

    def checkbox_move_tag_forward_changed(self, checkbox_move_tag_forward: QCheckBox):
        for table_items in self.status_table_items.values():
            checkbox = table_items["checkbox_move_tag_forward"]
            checkbox.blockSignals(True)
            if checkbox != checkbox_move_tag_forward:
                checkbox.setChecked(False)
            checkbox.blockSignals(False)
        self.status_table_changed()

    def status_table_changed(self):
        self.tableWidget_statuses.blockSignals(True)
        for status, table_items in self.status_table_items.items():
            status.name = table_items["name"].text()
            status.completed = table_items["checkbox_move_tag_forward"].isChecked()
            status.start_timer = table_items["checkbox_starts_timer"].isChecked()
        self.tableWidget_statuses.blockSignals(False)

    def add_status(self):
        if selected_tag := self.get_selected_tag():
            status = Status(f"Status{self.tableWidget_statuses.rowCount()}", {})
            selected_tag.add_status(status)
            self.load_status_table()

    def checkbox_enable_timer_changed(self):
        if selected_tag := self.get_selected_tag():
            selected_tag.attribute.is_timer_enabled = (
                self.checkBox_enable_timer.isChecked()
            )

    def checkbox_show_all_items_changed(self):
        if selected_tag := self.get_selected_tag():
            selected_tag.attribute.show_all_items = (
                self.checkBox_show_all_items.isChecked()
            )

    def next_flow_tag_message_changed(self):
        if selected_tag := self.get_selected_tag():
            selected_tag.attribute.next_flow_tag_message = (
                self.plainTextEdit_next_flow_tag_message.toPlainText()
            )

    def load_attributes(self):
        if selected_tag := self.get_selected_tag():
            self.groupBox_5.setTitle(f"Attributes for {selected_tag.name}")
            self.checkBox_enable_timer.setChecked(
                selected_tag.attribute.is_timer_enabled
            )
            self.checkBox_show_all_items.setChecked(
                selected_tag.attribute.show_all_items
            )
            self.plainTextEdit_next_flow_tag_message.setPlainText(
                selected_tag.attribute.next_flow_tag_message
            )

    def notes_changed(self):
        self.workspace_settings.notes = self.textEdit_notes.toPlainText()

    def clear_layout(self, layout: QHBoxLayout | QWidget) -> None:
        with contextlib.suppress(AttributeError):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        self.clear_layout(item.layout())

    def open_group_menu(self, menu: QMenu) -> None:
        menu.exec(QCursor.pos())

    def save(self):
        self.workspace_settings.save()

    def save_and_close(self):
        self.workspace_settings.save()
        self.accept()
