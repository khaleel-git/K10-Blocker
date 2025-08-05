import sys
import time
import os
import datetime
import json
import re

# Import all necessary libraries for both screen monitoring and GUI blocking.
import pyautogui
import pytesseract
import win32gui

from PyQt6.QtCore import Qt, QUrl, QTimer, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

# --- USER'S ORIGINAL CONFIGURATION ---
working_dir = "C:\\Users\\khale\\Documents\\K10-Blocker\\"
# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

# --- PyQt6 GUI SETUP FOR SCREEN BLOCKING ---

# Define a custom main window to handle the full-screen web view.
class WebViewWindow(QMainWindow):
    """
    A custom QMainWindow that displays a QWebEngineView in full-screen mode.
    The window is set to always be on top, blocking other screen content.
    """
    # Define a signal to emit when the window is closed
    closed = pyqtSignal()

    def __init__(self, url):
        """
        Initializes the window with a given URL.
        
        :param url: The URL to load in the web view.
        """
        super().__init__()

        # Set the window to be full-screen
        self.showFullScreen()
        
        # Set the window flags to keep it always on top.
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        # Create a QWidget to hold the layout for the browser and the button
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create a vertical layout
        layout = QVBoxLayout(central_widget)

        # Create a QWebEngineView widget to render the web page
        self.browser = QWebEngineView()
        
        # Load the specified URL.
        self.browser.setUrl(QUrl(url))
        
        # Add the browser to the layout.
        layout.addWidget(self.browser)
        
        # Create a button to allow the user to unblock the screen.
        unblock_button = QPushButton("Unblock Screen")
        unblock_button.setStyleSheet("background-color: #F44336; color: white; padding: 20px; font-size: 24px;")
        unblock_button.clicked.connect(self.close)
        
        # Add the button to the layout.
        layout.addWidget(unblock_button)
        
        # Connect the web view's 'loadFinished' signal to a function
        # to ensure the window is shown only after the page has loaded.
        self.browser.loadFinished.connect(self.show)
    
    def closeEvent(self, event):
        """
        Overrides the close event to emit a signal.
        """
        self.closed.emit()
        super().closeEvent(event)


# --- MAIN APPLICATION LOGIC ---

class ScreenMonitor(QMainWindow):
    """
    A hidden main window that monitors the screen using a QTimer.
    """
    def __init__(self, keywords):
        super().__init__()
        
        self.keywords = keywords
        self.blocking_window = None # Keep track of the blocking window
        
        # This window is not visible to the user. Its only purpose is to run the QTimer.
        self.setWindowTitle("K10 Blocker Monitor")
        self.hide()
        
        # Setup the QTimer to check the screen every 2 seconds.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_screen)
        self.timer.start(2000) # 2000 milliseconds = 2 seconds
        
        print(f"K10 Database: {len(self.keywords)} keywords loaded.")
        print("Screen monitoring started...")

    def get_active_window_title(self):
        """Returns the title of the currently active window."""
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        return title

    def check_screen(self):
        """
        This function is called by the QTimer to check the screen.
        """
        try:
            # Take a screenshot
            screenshot = pyautogui.screenshot()

            # Use Tesseract to do OCR on the screenshot
            text_on_screen = pytesseract.image_to_string(screenshot)

            # Check if any keyword is present in the extracted text
            for keyword in self.keywords:
                # Use regular expression to ensure that the keyword is a complete word
                pattern = r'\b' + re.escape(keyword) + r'\b'
                if re.search(pattern, text_on_screen, re.IGNORECASE):
                    window_title = self.get_active_window_title()
                    print(f"Keyword '{keyword}' found on the screen in window: '{window_title}'!")
                    
                    # Log the hit keyword
                    with open(working_dir + "hit_keywords.txt", "a") as fd:
                        fd.write(f"{keyword}, {window_title}, {datetime.datetime.now()} \n")

                    print("Blocking screen with a full-screen web page...")
                    
                    # --- LAUNCH THE BLOCKING GUI ---
                    # Stop the timer so we don't open multiple windows.
                    self.timer.stop()
                    
                    # URL to open and block the screen with.
                    # You can change this to any valid URL you want.
                    web_page_url = 'https://www.youtube.com/watch?v=iO6jYmuJCuA'
                    
                    # Create and show the blocking web view window.
                    self.blocking_window = WebViewWindow(web_page_url)
                    
                    # Connect the blocking window's closed signal to a function
                    # that will restart the timer.
                    self.blocking_window.closed.connect(self.resume_monitoring)

                    # Return from the function to prevent further checks
                    return

        except Exception as ex:
            # Handle any exceptions from pyautogui or pytesseract
            print(f"An error occurred: {ex}")
            # Do not stop the timer on an error, it will just try again next interval.

    def resume_monitoring(self):
        """
        Restart the timer after the blocking window is closed.
        """
        self.blocking_window = None
        self.timer.start()
        print("Screen monitoring resumed...")

# --- MAIN EXECUTION BLOCK ---

if __name__ == '__main__':
    # Fix for DPI scaling issues on Windows by setting an environment variable.
    # This must be done before the QApplication is created.
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"

    # Create the QApplication instance once at the very start
    app = QApplication(sys.argv)
    
    # Do not quit the application when the last window is closed.
    # This is crucial for keeping the hidden monitor window alive.
    app.setQuitOnLastWindowClosed(False)

    # Load the contents of the first JSON file into a dictionary
    with open(working_dir + "single_bad_keywords_cloud.json", "r") as fd1:
        single_keyword_occean = json.load(fd1)

    # Load the contents of the second JSON file into another dictionary
    with open(working_dir + "multi_bad_keywords_cloud.json", "r") as fd2:
        multi_keyword_occean = json.load(fd2)

    single_list = []
    for k,v in single_keyword_occean.items():
        for w in single_keyword_occean[k]:
            single_list.append(w)

    multi_list = []
    for k,v in multi_keyword_occean.items():
        for w in multi_keyword_occean[k]:
            multi_list.append(w)
    
    keywords = single_list + multi_list

    # Create the screen monitoring window and start the event loop
    monitor = ScreenMonitor(keywords)
    
    # Start the application's event loop. This is the main blocking call.
    sys.exit(app.exec())
