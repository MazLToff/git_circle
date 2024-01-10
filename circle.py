import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Git и случайные окружности')
        self.setGeometry(100, 100, 400, 400)
        self.button = QPushButton('Кнопка', self)
        self.button.setGeometry(150, 10, 100, 30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        diameter = randint(10, 100)  # Random diameter
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))  # Random color
        qp.setBrush(color)
        qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
