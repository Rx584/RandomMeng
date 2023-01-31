from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_meng import *
import sys

class MengT(QWidget,Ui_MengT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MengT()
    sys.exit(app.exec())