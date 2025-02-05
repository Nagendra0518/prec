import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
import numpy as np

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the main window
        self.setWindowTitle("PyQt Timer with Inline Buttons and Text Fields")
        self.setGeometry(100, 100, 500, 400)

        # Set up a label for displaying messages
        self.label = QLabel("Hello, Nagendra", self)
        self.label.move(50, 20)

        # Set up a label to display the timer
        self.timer_label = QLabel("00:00:00", self)  # Changed to show hours, minutes, seconds
        self.timer_label.move(350, 20)  # Position timer on the right
        self.timer_label.setStyleSheet("font-size: 24px; color: blue;")

        # Initialize timer variables
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0  # Start from 0 for count-up timer

        # Create an additional timer for updating random values
        self.value_timer = QTimer(self)
        self.value_timer.timeout.connect(self.populate_text_fields)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(0)  # Set the space between buttons to 0 pixels
        button_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a tighter layout

        # Create inline buttons with colors and connect them to functions
        button_layout.addWidget(self.create_button("START", "green", self.start_action))
        button_layout.addWidget(self.create_button("STOP", "violet", self.stop_action))
        button_layout.addWidget(self.create_button("RESET", "red", self.reset_action))
        button_layout.addWidget(self.create_button("SHOW GRAPHS", "blue", self.show_graphs))
        button_layout.addWidget(self.create_button("HOME", "purple", self.home_action))  # Home button

        # Create a vertical layout for the main window
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.timer_label)
        self.main_layout.addLayout(button_layout)  # Add button layout
        self.main_layout.addStretch()  # Push everything up

        # Create labeled text fields to display random numbers
        self.text_fields = []
        self.main_layout.addLayout(self.create_text_fields_layout())  # Add text fields layout

        # Set the main layout to a central widget
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        # Initialize data storage for graphing
        self.data = {f"Field {i + 1}": [] for i in range(4)}  # Store random values for four fields
        self.time_points = []  # To store time points for the x-axis

        # Initialize name fields as None
        self.name_fields_layout = None

    def create_button(self, text, color, action):
        """Helper function to create a colored button."""
        button = QPushButton(text)
        button.setStyleSheet(f"background-color: {color}; color: white; font-weight: bold;")
        button.setFixedWidth(100)  # Set a fixed width for the buttons
        button.clicked.connect(action)
        return button

    def create_text_fields_layout(self):
        """Create a vertical layout for text fields."""
        layout = QVBoxLayout()
        labels = ["Field 1:", "Field 2:", "Field 3:", "Field 4:"]  # Define names for each text field

        for i, label_text in enumerate(labels):
            # Text field
            text_field = QLineEdit(self)
            text_field.setReadOnly(True)  # Make text field read-only
            self.text_fields.append(text_field)

            # Name label
            name_label = QLabel(label_text, self)
            layout.addWidget(name_label)
            layout.addWidget(text_field)

        return layout

    def update_timer(self):
        """Update the timer display each second.""" 
        self.time_elapsed += 1
        hours = self.time_elapsed // 3600
        minutes = (self.time_elapsed % 3600) // 60
        seconds = self.time_elapsed % 60
        self.timer_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")  # Format as HH:MM:SS

    def start_action(self):
        """Start the timer counting up from 0 and fetch random numbers."""
        if not self.all_name_fields_filled():  # Ensure all name fields are filled before starting
            self.show_warning("Please fill in all name fields before starting the timer.")
            return

        if not self.timer.isActive():  # Start only if not already running
            self.timer.start(1000)  # Update timer every second
            self.value_timer.start(5000)  # Update random values every 5 seconds
            self.label.setText("Timer started")
            self.populate_text_fields()  # Fetch and display random numbers immediately

    def show_warning(self, message):
        """Show a warning message box."""
        QMessageBox.warning(self, "Warning", message)

    def stop_action(self):
        """Stop the timer temporarily."""
        if self.timer.isActive():
            self.timer.stop()
            self.value_timer.stop()  # Stop the value update timer
            self.label.setText("Timer stopped")

    def reset_action(self):
        """Reset the timer to 0 and stop it."""
        self.timer.stop()
        self.value_timer.stop()  # Stop the value update timer
        self.time_elapsed = 0  # Reset to 0
        self.timer_label.setText("00:00:00")  # Reset timer display
        self.label.setText("Timer reset")
        self.clear_text_fields()  # Clear the text fields on reset

        # Reset data for graphs
        self.data = {f"Field {i + 1}": [] for i in range(4)}  # Clear data for graphing
        self.time_points = []  # Clear time points

    def abort_action(self):
        """Stop the timer and clear the display."""
        self.timer.stop()
        self.value_timer.stop()  # Stop the value update timer
        self.time_elapsed = 0
        self.timer_label.setText("00:00:00")  # Reset timer display
        self.label.setText("Timer aborted")
        self.clear_text_fields()  # Clear the text fields on abort

    def home_action(self):
        """Reset the application to its home state with name fields."""
        self.timer.stop()
        self.value_timer.stop()  # Stop the value update timer
        self.time_elapsed = 0
        self.timer_label.setText("00:00:00")  # Reset timer display
        self.label.setText("Welcome Home")
        self.clear_text_fields()  # Clear the text fields on home action
        self.create_name_fields()  # Create name fields in home action

    def clear_text_fields(self):
        """Clear the text fields."""
        for text_field in self.text_fields:
            text_field.clear()

    def create_name_fields(self):
        """Create text fields for names: First Name, Middle Name, Last Name, Preferred Name."""
        # Check if the name fields already exist
        if self.name_fields_layout is not None:
            return  # Return if name fields are already created

        # Create new layout for name fields
        self.name_fields_layout = QVBoxLayout()
        name_labels = ["First Name:", "Middle Name:", "Last Name:", "Preferred Name:"]

        self.name_fields = []
        for label_text in name_labels:
            name_label = QLabel(label_text, self)
            name_field = QLineEdit(self)
            self.name_fields.append(name_field)
            self.name_fields_layout.addWidget(name_label)
            self.name_fields_layout.addWidget(name_field)

        # Add the new layout to the main layout of the central widget
        self.main_layout.addLayout(self.name_fields_layout)

    def all_name_fields_filled(self):
        """Check if all name fields are filled."""
        if self.name_fields_layout is None:
            return False  # No name fields present
        for name_field in self.name_fields:
            if not name_field.text().strip():  # Check if the field is empty
                return False
        return True

    def populate_text_fields(self):
        """Generate random numbers and populate text fields."""
        numbers = [random.randint(1, 100) for _ in range(4)]  # Generate four random numbers

        # Populate text fields with random numbers
        for i, number in enumerate(numbers):
            self.text_fields[i].setText(str(number))  # Display the random number in the QLineEdit
            self.data[f"Field {i + 1}"].append(number)  # Store number for graphing
        
        # Update time points for x-axis
        self.time_points.append(len(self.data["Field 1"]) - 1)

    def show_graphs(self):
        """Display graphs for the random numbers."""
        if not all(len(values) > 0 for values in self.data.values()):  # Check if there's data to plot
            self.label.setText("Not enough data to show graphs.")
            return
        
        plt.figure(figsize=(10, 8))
        x = np.array(self.time_points)  # Time in seconds based on the number of updates

        for i, (label, values) in enumerate(self.data.items()):
            plt.subplot(2, 2, i + 1)  # Create a 2x2 subplot
            plt.plot(x, values, marker='o')  # Plot with markers
            plt.title(label)
            plt.xlabel('Time (5s intervals)')
            plt.ylabel('Random Values')
            plt.xticks(x)  # Show x ticks for each time point
            plt.ylim(0, 100)  # Set y-axis limits for better visualization

        plt.tight_layout()
        plt.show()  # Display the plots

def main():
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
