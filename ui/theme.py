import contextlib
import os

from PyQt6 import QtGui

THEME_PATH = f"{os.getcwd()}/ui/"

STYLE_SHEET_PATH_DICT = {"dark": os.path.join(THEME_PATH, "dark_theme.css")}

DEFAULT_ICON_PATH = "icons"
CURRENT_ICON_PATH = os.path.join(THEME_PATH, DEFAULT_ICON_PATH).replace("\\", "/")


def set_theme(app, theme: str = "default") -> None:
    '''This function use to set theme for "QApplication", support for "PySide2" and "PyQt5"'''
    # Get the name of the library that the app object belongs to
    lib_name = app.__module__.split(".")[0]

    # Import the QtGui module from the library with the name stored in lib_name
    # QtGui = __import__(lib_name).QtGui

    # Check if the theme is set to 'dark'
    if theme == "dark":
        set_pallete(app, theme)
    elif theme == "default":
        # Set the application style to an empty string, which resets it to the default style
        app.setStyle(str())

        # Reset the application palette to the default palette
        app.setPalette(QtGui.QPalette())


def set_pallete(app, theme):
    # Set the application style to 'Fusion'
    with contextlib.suppress(TypeError):
        app.setStyle("fusion")
    # Create a palette with dark colors
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(44, 44, 44))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor(246, 246, 246))
    palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(29, 29, 29))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtGui.QColor(210, 210, 210))
    palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor(210, 218, 218))
    palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(44, 44, 44))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor(210, 210, 210))
    palette.setColor(QtGui.QPalette.ColorRole.BrightText, QtGui.QColor(246, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(110, 120, 125, 127))
    # Apply the dark palette to the application
    app.setPalette(palette)

    # set dark theme style sheet
    with open(STYLE_SHEET_PATH_DICT[theme], "r") as style_sheet:
        app.setStyleSheet(style_sheet.read().replace(DEFAULT_ICON_PATH, CURRENT_ICON_PATH))
