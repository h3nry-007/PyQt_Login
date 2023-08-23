from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

import database as db 

class UserLoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Login")
        self.setGeometry(200, 200, 300, 150)

        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit(self)

        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user_Found = False
        for u_id, u_info in db.user_data.items():
            if username == u_info["Name"] and password == u_info["Password"]:
                QMessageBox.information(self, "Login Successful", f"Welcom {username}")
                user_Found = True
                break
        if not user_Found:
            QMessageBox.warning(self, "Login Failed ", "Username or Password is incorrect!")

def user_login():
    dialog = UserLoginDialog()
    dialog.exec_()
