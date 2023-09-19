import sys
from PyQt5.QtCore import Qt  # Import the Qt module
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication([])

# Create a main window
window = QMainWindow()
window.setWindowTitle("Hello, World!")

# Create a label widget with the desired text
label = QLabel("Hello, World!")
label.setAlignment(Qt.AlignCenter)

# Set the label as the central widget of the main window
window.setCentralWidget(label)

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec_())