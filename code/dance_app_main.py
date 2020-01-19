from PyQt5.QtWidgets import QApplication, QMainWindow
from code.dance_app_uis.dance_app_main_window import Ui_DanceAppMainWindow
from code.add_dance_code import *
from code.modify_dance_code import *
from code.move_challenge_code import *
import sys


class DanceAppWindow(QMainWindow):
    def __init__(self):
        super(DanceAppWindow, self).__init__()
        self.ui = Ui_DanceAppMainWindow()
        self.ui.setupUi(self)
        self.assign_slots()

        self.add_dance_window = None
        self.modify_dance_window = None
        self.challege_window = None

    def assign_slots(self):
        self.ui.add_move_pushButton.clicked.connect(self.show_add_window)
        self.ui.modify_move_pushButton.clicked.connect(self.show_modify_window)
        self.ui.challenge_pushButton.clicked.connect(self.show_challenge_window)

    def show_add_window(self):
        add_dance_window.show()

    def show_modify_window(self):
        modify_dance_window.show()

    def show_challenge_window(self):
        select_window.show()


# making sure I get error messages.
_excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    _excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
dance_app_window = DanceAppWindow()
dance_app_window.show()
sys.exit(app.exec())
