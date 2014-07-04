from PyQt.QtGui import *

class ManualGrowDialog(QDialog):
    """this class provides a dialog window to ask for light and water values"""
    #constructor
    def __init__(self):
        super().__init__()

        self.water_spinbox = QSpinBox()
        self.light_spinbox = QSpinBox()

        self.water_spinbox.setRange(0,10)
        self.light_spinbox.setRange(0,10)

        self.water_spingbox.setSuffix(" Water")
        self.light_spingbox.setSuffix(" Light")

        self.water_spinbox.setValue(1)
        self.light_spinbox.setValue(1)

        self.submit_button = QPushButton("Enter Values")

        self.dialog_layout= QVBoxLayout()
        self.dialog_layout.addWidget(self.light_spinbox)
        self.dialog_layout.addWidget(self.water_spingbox)
        self.dialog_layout.addWidget(self.submit_button)

        self.setLayout(self.dialog_layout)

        #connections
        self.submit_button.clicked.connect(self.close)

    def values(self):
        return int(self.light_spingbox.value()),int(self.water_spinbox.value())

        
