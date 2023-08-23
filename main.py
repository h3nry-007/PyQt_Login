#! /usr/bin/env python3 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import admin as ad 
import student as st 

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Program")
        self.setGeometry(100, 100, 300, 300) # x, y, width, height

        admin_button = QPushButton("Admin Login", self)
        admin_button.setGeometry(50, 50, 200, 40)
        admin_button.clicked.connect(self.admin_login)

        user_button = QPushButton("User Login", self)
        user_button.setGeometry(50, 100, 200, 40)
        user_button.clicked.connect(self.user_login)
        
        exit_button = QPushButton("Exit", self)
        exit_button.setGeometry(50, 150, 200, 40)
        exit_button.clicked.connect(self.exit_)

    def admin_login(self):
        ad.admin_login()

    def user_login(self):
        st.user_login()
    def exit_(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
