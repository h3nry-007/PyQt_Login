from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

import database as db
import student_enroll as se
class AdminLoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login")
        self.setGeometry(200, 200, 300, 150)

        self.admin_name_label = QLabel("Admin Name:", self)
        self.admin_name_input = QLineEdit(self)

        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.admin_name_label)
        layout.addWidget(self.admin_name_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):

        username = self.admin_name_input.text()
        password = self.password_input.text()
        user_Found = False
        for u_id, u_info in db.admin_data.items():
            if username == u_info["Name"] and password == u_info["Password"]:
                QMessageBox.information(self, "Login Successful",f"Welcome {username}")
                user_Found = True
                se.stu_Enroll()
        if not user_Found:
            QMessageBox.warning(self,"Login Failed", "User name or password is incorrect")
            
                
def admin_login():
    dialog = AdminLoginDialog()
    dialog.exec_()
