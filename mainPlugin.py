from PyQt5.QtWidgets import QAction, QDockWidget
from .dynamic_plot_widget import DynamicPlotWidget 
from PyQt5.QtCore import Qt

class MainPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction("Open Dynamic Plot", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        self.widget = DynamicPlotWidget()
        self.dock_widget = QDockWidget()
        self.dock_widget.setWidget(self.widget)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)
