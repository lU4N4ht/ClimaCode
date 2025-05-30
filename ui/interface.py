from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QMessageBox
)
from PyQt5.QtGui import QPixmap, QPalette, QLinearGradient, QColor, QBrush
from PyQt5.QtCore import Qt
import sys
from controllers.controller import buscar_clima_por_cidade


class ClimaCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ClimaCode")
        self.setFixedSize(370, 800)
        self.setStyleSheet("font-family: 'Inter';")
        self.init_ui()

    def init_ui(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor(30, 94, 206))
        gradient.setColorAt(0.74, QColor(91, 161, 225))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.png").scaled(131, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setAlignment(Qt.AlignHCenter)
        logo.setContentsMargins(0, 68, 0, 0)
        layout.addWidget(logo)

        container2 = QWidget()
        container2.setFixedHeight(580)
        container2.setStyleSheet("""
            background-color: white;
            border-top-left-radius: 30px;
            border-top-right-radius: 30px;
        """)
        container2_layout = QVBoxLayout(container2)
        container2_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        container2_layout.setContentsMargins(28, 28, 28, 28)
        container2_layout.setSpacing(45)

        line = QFrame()
        line.setFixedSize(100, 7)
        line.setStyleSheet("background-color: #3A98DE; border-radius: 10px;")
        container2_layout.addWidget(line, alignment=Qt.AlignCenter)

        earth = QLabel()
        earth.setPixmap(QPixmap("assets/earth.png").scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        earth.setAlignment(Qt.AlignCenter)
        container2_layout.addWidget(earth)

        text_label = QLabel("Busque por uma cidade:")
        text_label.setStyleSheet("color: #3A98DE; font-size: 20px; font-weight: 900;")
        text_label.setAlignment(Qt.AlignCenter)
        container2_layout.addWidget(text_label)

        self.input = QLineEdit()
        self.input.setFixedSize(250, 41)
        self.input.setStyleSheet("""
            border: 1px solid #1E5ECE;
            border-radius: 5px;
            padding: 0 14px;
        """)
        container2_layout.addWidget(self.input)

        self.button = QPushButton("Buscar")
        self.button.setFixedSize(110, 40)
        self.button.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,
                stop:0 rgba(30, 94, 206, 255), stop:0.74 rgba(91, 161, 225, 255));
            color: white;
            font-size: 16px;
            font-weight: 900;
            border-radius: 5px;
        """)
        self.button.clicked.connect(self.buscar_clima)
        container2_layout.addWidget(self.button, alignment=Qt.AlignCenter)

        layout.addWidget(container2)

    def buscar_clima(self):
        cidade = self.input.text().strip()
        if not cidade:
            QMessageBox.warning(self, "Atenção", "Digite o nome de uma cidade válida.")
            return

        resultado = buscar_clima_por_cidade(cidade)
        if "erro" in resultado:
            QMessageBox.critical(self, "Erro", resultado["erro"])
        else:
            QMessageBox.information(self, "Clima Atual", resultado["mensagem"])


def iniciar_interface():
    app = QApplication(sys.argv)
    window = ClimaCodeApp()
    window.show()
    sys.exit(app.exec_())
