from PyQt5.QtWidgets import QVBoxLayout
from .dynamic_plot_widget import DynamicPlotWidget

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.plot_widget = DynamicPlotWidget(self)

        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)
