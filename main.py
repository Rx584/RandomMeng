from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_meng import *
import sys,random

class MengT(QWidget,Ui_MengT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.creat_meng)
        self.setWindowIcon(QIcon("icon.ico"))
        self.show()

    def creat_meng(self):
        
        give = ""
        count = 200
        count = int(self.le_count.text())
        
        for i in range(count):
            enum = random.randint(0,3)
            if (enum == 0):
                give+="A"
            elif(enum == 1):
                give+="B"
            elif(enum == 2):
                give+="C"
            elif(enum == 3):
                give+="D"
        self.tb_view.setText(give)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MengT()
    sys.exit(app.exec())