import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from iterator import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("by Лысый")
        self.setFixedSize(1280, 720)

        self.image_label = QLabel(self)
        self.image_label.resize(1280, 600)
        self.image_label.setAlignment(Qt.AlignCenter)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.image_label)
        self.setCentralWidget(central_widget)
        #создали вертикальный интерфейс

        self.button_previous = QPushButton("<< Back", self)
        self.button_previous.setFixedSize(450, 80)
        self.button_previous.move(0, 640)
        self.button_previous.setStyleSheet('background: rgb(51, 255, 255);')
        self.button_previous.clicked.connect(self.back_image)

        self.button_path = QPushButton("Select CSV File", self)
        self.button_path.setFixedSize(380, 80)
        self.button_path.move(450, 640)
        self.button_path.setStyleSheet('background: rgb(0, 255, 255);')
        self.button_path.clicked.connect(self.select_csv_file)

        self.button_next = QPushButton("Next >>", self)
        self.button_next.setFixedSize(450, 80)
        self.button_next.move(830, 640)
        self.button_next.setStyleSheet('background: rgb(51, 255, 255);')
        self.button_next.clicked.connect(self.next_image)

        self.iterator = None


    def select_csv_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите CSV файл с путями к изображениям", "", "CSV Files (*.csv)")
        if filename:
            self.iterator = ImageIterator(filename)
            pixmap = QPixmap(self.iterator.get_current_element())
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))


    def next_image(self):
        if self.iterator and len(self.iterator.images) != 0:
            try:
                next_image_path = self.iterator.__next__()
                pixmap = QPixmap(next_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                pass


    def back_image(self):
        if self.iterator is not None:
            try:
                back_image_path = self.iterator.__back__()
                pixmap = QPixmap(back_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                pass


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
