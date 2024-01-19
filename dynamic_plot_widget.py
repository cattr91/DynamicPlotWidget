from PyQt5.QtWidgets import QWidget
from .output import Ui_DynamicPlotDialogBase

class DynamicPlotWidget(QWidget, Ui_DynamicPlotDialogBase):
    def __init__(self, parent=None):
        super(DynamicPlotWidget, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.update_plot)

    def update_plot(self):
        # Clear the existing plot
        self.PlotWidget.clear()

        # Get the text from the line edit widget
        text = self.lineEdit.text()

        # Convert the text to a list of integers
        data = [int(i) for i in text.split()]

        # Plot the data
        self.PlotWidget.plot(data)
