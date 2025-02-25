import sys
import random
import string
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 300)

        # Заголовок
        self.label = QLabel("Password Generator For You", self)
        self.label.setAlignment(Qt.AlignCenter)

        # Поле для пароля
        self.password_input = QLineEdit(self)
        self.password_input.setReadOnly(True)

        # Кнопка для генерации пароля
        self.generate_button = QPushButton("Generate Password", self)
        self.generate_button.clicked.connect(self.generate_password)

        # Кнопка "Clear"
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_password)

        # Кнопка "Help"
        self.help_button = QPushButton("Help", self)
        self.help_button.clicked.connect(self.show_help)

        # Вертикальный layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.help_button)
        self.setLayout(layout)

    def generate_password(self):
        # Генерация случайного пароля
        length = 12  # Длина пароля
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        self.password_input.setText(password)

    def clear_password(self):
        # Очистка поля для пароля
        self.password_input.clear()

    def show_help(self):
        # Окно помощи
        help_dialog = HelpDialog()
        help_dialog.exec()

class HelpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.setGeometry(150, 150, 300, 200)

        # Текст помощи
        help_label = QLabel("This is a simple password generator. Click 'Generate Password' to create a random password.", self)
        help_label.setAlignment(Qt.AlignCenter)

        # Layout для диалогового окна
        layout = QVBoxLayout()
        layout.addWidget(help_label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
