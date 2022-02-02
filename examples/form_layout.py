#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormatLayout')

layout = QFormLayout()
layout.addRow('Name: ', QLineEdit())
layout.addRow('Age: ', QLineEdit())
layout.addRow('Job: ', QLineEdit())
layout.addRow('Hobbies: ', QLineEdit())
window.setLayout(layout)
window.show()

sys.exit(app.exec_())
