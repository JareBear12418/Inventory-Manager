from enum import Enum, auto

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QAbstractItemView, QTableWidgetItem

from ui.custom_widgets import CustomTableWidget


class AutoNumber(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count


class LaserCutTableColumns(AutoNumber):
    PICTURE = auto()
    PART_NAME = auto()
    BENDING_FILES = auto()
    WELDING_FILES = auto()
    CNC_MILLING_FILES = auto()
    MATERIAL = auto()
    THICKNESS = auto()
    UNIT_QUANTITY = auto()
    QUANTITY = auto()
    SHELF_NUMBER = auto()
    PAINTING = auto()
    PAINT_SETTINGS = auto()
    FLOW_TAG = auto()
    EXPECTED_TIME_TO_COMPLETE = auto()
    NOTES = auto()


class LaserCutPartsPlanningTableWidget(CustomTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.row_height = 70

        editable_columns = [
            LaserCutTableColumns.PART_NAME,
            LaserCutTableColumns.UNIT_QUANTITY,
            LaserCutTableColumns.NOTES,
            LaserCutTableColumns.SHELF_NUMBER,
        ]

        self.setShowGrid(True)
        self.setSortingEnabled(False)
        self.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.set_editable_column_index([col.value for col in editable_columns])

        headers = {
            "Picture": LaserCutTableColumns.PICTURE.value,
            "Part Name": LaserCutTableColumns.PART_NAME.value,
            "Bending Files": LaserCutTableColumns.BENDING_FILES.value,
            "Welding Files": LaserCutTableColumns.WELDING_FILES.value,
            "CNC/Milling Files": LaserCutTableColumns.CNC_MILLING_FILES.value,
            "Material": LaserCutTableColumns.MATERIAL.value,
            "Thickness": LaserCutTableColumns.THICKNESS.value,
            "Unit Quantity": LaserCutTableColumns.UNIT_QUANTITY.value,
            "Quantity": LaserCutTableColumns.QUANTITY.value,
            "Shelf #": LaserCutTableColumns.SHELF_NUMBER.value,
            "Painting": LaserCutTableColumns.PAINTING.value,
            "Paint Settings": LaserCutTableColumns.PAINT_SETTINGS.value,
            "Flow Tag": LaserCutTableColumns.FLOW_TAG.value,
            "Expected time\nto complete": LaserCutTableColumns.EXPECTED_TIME_TO_COMPLETE.value,
            "Notes": LaserCutTableColumns.NOTES.value,
        }

        self.setColumnCount(len(headers))
        for header, column in headers.items():
            self.setHorizontalHeaderItem(column, QTableWidgetItem(header))

        self.setStyleSheet("border-color: transparent;")
