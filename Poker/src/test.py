from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets.QWidget import window


class YourClass:
    def __init__(self):
        self.card_6 = QLabel()
        self.set_gray_frame()

    def set_gray_frame(self):
        self.card_6.setStyleSheet("border: 2px solid gray;")
        self.card_6.clear()

    def set_pixmap(self, image_path):
        self.pixmap = QPixmap(image_path)
        if not self.pixmap.isNull():  # Проверка на успешную загрузку
            self.pixmap = self.pixmap.scaled(self.new_width, self.new_height)
            self.card_6.setPixmap(self.pixmap)
            self.card_6.update()  # Обновляем QLabel
        else:
            print("Ошибка: Не удалось загрузить изображение.")

    def reset_label(self):
        self.card_6.clear()
        self.set_gray_frame()

