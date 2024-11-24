import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def show_winner_window(player_name):
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = QWidget()
    window.setWindowTitle("Winner Announcement")

    # Создаем метку с текстом
    label = QLabel(f"{player_name} wins round")

    # Устанавливаем вертикальный макет
    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)

    # Устанавливаем размер окна и показываем его
    window.resize(300, 100)
    window.show()

    time.sleep(2)
    # Запускаем приложение
    sys.exit(app.exec())
