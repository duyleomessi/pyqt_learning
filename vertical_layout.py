#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Button Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Botton'))
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
