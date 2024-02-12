import pyautogui
import pytesseract
import re
import time
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\emahkah\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def find_and_close_window(keywords):
    while True:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Use Tesseract to do OCR on the screenshot
        text_on_screen = pytesseract.image_to_string(screenshot)

        # Check if any keyword is present in the extracted text
        for keyword in keywords:
            # Use regular expression to ensure that the keyword is a complete word
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, text_on_screen, re.IGNORECASE):
                print(f"Keyword '{keyword}' found on the screen!")
                print(f"{keyword} blocked!")
                # Simulate pressing Alt+F4 to close the active window
                pyautogui.hotkey('alt', 'f4')
                print("Window closed.")
                # return  # Exit the function after closing the window

        # print("No keywords found on the screen. Waiting for the next check...")
        # time.sleep(2)

# Replace 'bad_words.txt' with the path to your keyword file
keyword_occean = set()
keyword_file_path = 'C:\\Users\\emahkah\\OneDrive - Ericsson\\Documents\\GitHub\\Khaleel_Por_Blocker\\lists\\'
for folder in os.listdir(keyword_file_path):
    print(f"folder: {folder}")
    for file in os.listdir(keyword_file_path + folder):
        with open(keyword_file_path + folder + "\\" + file, "r") as read:
            for line in read:
                # print(line.strip())
                keyword_occean.add(line)

# Call the function with the set of keywords
while True:
    time.sleep(2)
    while True:
        time.sleep(2)
        find_and_close_window(keyword_occean)
