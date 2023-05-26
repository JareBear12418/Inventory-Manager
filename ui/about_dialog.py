from PyQt5 import uic
from PyQt5.QtCore import QFile, Qt, QTextStream
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget

from ui.theme import set_theme
from utils.dialog_icons import Icons
from utils.json_file import JsonFile

settings_file = JsonFile(file_name="settings")


class AboutDialog(QWidget):
    """
    About dialog
    """

    def __init__(self, parent, title: str, version: str, updated: str, home: str) -> None:
        """
        It's a function that loads the about dialog

        Args:
          title (str): str = "My App"
          version (str): str = "0.0.1"
          updated (str): str = "2020-04-20"
          home (str): str = "https://github.com/michael-k-zhang/py-pomodoro"
        """
        super(AboutDialog, self).__init__(parent)
        uic.loadUi("ui/about_dialog.ui", self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(Icons.icon))
        self.setFixedSize(550, 400)

        self.theme: str = (
            "dark" if settings_file.get_value(item_name="dark_mode") else "light"
        )

        pixmap = QPixmap("icons/icon.png")
        scaled_pixmap = pixmap.scaled(self.lblIcon.size(), Qt.KeepAspectRatio)

        self.lblIcon.setFixedSize(128, 128)
        self.lblIcon.setPixmap(scaled_pixmap)

        self.lblVersion.setText(f"Build time: {updated}")

        with open("LICENSE", "r") as license_file:
            self.lblLicense.setText(license_file.read())

        self.lblTitle.setText(f"{title} {version}")

        self.lblHome.setText(
            f"Home: <a style='text-decoration:none;color:yellow'href='{home}'>{home}</a>"
        )

        self.scrollArea.setStyleSheet("border: 0px")

        self.btnClose.clicked.connect(self.close)

        self.load_theme()


    def load_theme(self) -> None:
        """
        It loads the stylesheet.qss file from the theme folder
        """
        set_theme(self, theme='dark')
