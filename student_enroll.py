import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class Enroll(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Enroll Student")
        self.setGeometry(200, 200, 400, 500)
        
        
def stu_Enroll():
    dialog = Enroll()
    dialog.exec_()