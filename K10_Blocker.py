import pyautogui
import pytesseract
import re
import time
import os
import win32gui
import json

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\emahkah\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return title

# sing_bad_words = ['pornography','xnxx','xvideos','anal sex','porn']
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
                window_title = get_active_window_title()
                print(f"Keyword '{keyword}' found on the screen in window: '{window_title}'!\n")
                with open("hit_keywords.txt", "a") as fd:
                    fd.write(f"{keyword} blocked! on Screen: {window_title} \n")
                # Simulate pressing Alt+F4 to close the active window
                if window_title not in ['K10_Blocker',r'C:\Users\emahkah\OneDrive - Ericsson\Documents\GitHub\Khaleel_Por_Blocker\dist\K10_Blocker\K10_Blocker.exe']:
                    pyautogui.hotkey('alt', 'f4')
                # print("Window closed.")
                # return  # Exit the function after closing the window

        # print("No keywords found on the screen. Waiting for the next check...")
        time.sleep(2)


# Load the contents of the first JSON file into a dictionary
with open("single_bad_keywords_cloud.json", "r") as fd1:
    single_keyword_occean = json.load(fd1)

# Load the contents of the second JSON file into another dictionary
with open("multi_bad_keywords_cloud.json", "r") as fd2:
    multi_keyword_occean = json.load(fd2)


single_list = []
for k,v in single_keyword_occean.items():
    for w in single_keyword_occean[k]:
        single_list.append(w)

multi_list = []
for k,v in multi_keyword_occean.items():
    for w in multi_keyword_occean[k]:
        multi_list.append(w)

print(f"single_list: {len(single_list)}")
print(f"multi_list: {len(multi_list)}")

# # Call the function with the set of keywords
# while True:
#     time.sleep(2)
#     find_and_close_window(keyword_occean)
