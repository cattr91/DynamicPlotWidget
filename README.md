# DynamicallyPlotWidget

The `DynamicallyPlotWidget` is a custom widget designed for creating dynamic or real-time plots in your application.

We started building this plugin by following this [guide](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/).

## Getting Started

These instructions will guide you on how to install and use the `DynamicallyPlotWidget`.

### Prerequisites

- Python 3.x
- Qt Creator
- PySide2
- Plotly (optional for plotting)

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
The DynamicallyPlotWidget can be used as follows:

```
# Import the DynamicallyPlotWidget
from your_module import DynamicallyPlotWidget

# Create an instance of the widget
plot_widget = DynamicallyPlotWidget()

# Use the widget in your application
# ...
```

## Development
The development of this widget involved creating a UI with Qt Creator, converting it to Python, and then adding functionality.

### Creating the UI

1. Open Qt Creator and create a new project.
2. Design your UI by dragging and dropping widgets from the widget box onto the form.
3. Save your UI as a `.ui` file.

### Converting the UI to Python
5. Use the `pyside2-uic` tool to convert the `.ui` file to a Python script:

```
pyside2-uic mainwindow.ui > ui_mainwindow.py
```

### Adding Functionality

1. Import the generated Python script into your main Python file.
2. Create a new class that inherits from both `QMainWindow` and your UI class.
3. Implement the functionality in this new class.


## License
This project is licensed under the MIT License - see the LICENSE.md file for details