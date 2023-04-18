import pyautogui
import pyperclip

# Use the hotkey combination 'Win + R' to open the Run dialog box
pyautogui.hotkey('win', 'r')
# Type 'control panel' in the Run dialog box and press 'Enter' to open the Control Panel
pyautogui.write('control panel')
pyautogui.press('enter')

# Wait for the Control Panel to open and then use the hotkey combination 'Ctrl + F' to open the search bar
pyautogui.sleep(1)
pyautogui.hotkey('ctrl', 'f')

# Type 'view network status' in the search bar and wait for a moment
pyautogui.write('view network status')
pyautogui.sleep(1)
# Click on the search result and press 'Enter'
pyautogui.leftClick()
pyautogui.hotkey("enter")
# Wait for a moment and then click again and press 'Enter'
pyautogui.sleep(1)
pyautogui.leftClick()
pyautogui.hotkey("enter")
# Wait for a moment and then press 'Tab'
pyautogui.sleep(1)
pyautogui.hotkey("tab")
# Wait for a moment and then press 'Enter'
pyautogui.sleep(1)

pyautogui.hotkey("enter")
# Wait for a moment
pyautogui.sleep(1)

# Switch to the previous tab using the hotkey combination 'Ctrl + Shift + Tab'
pyautogui.hotkey('ctrl', 'shift', 'tab')
# Wait for a moment and then locate the center of the image "show_password.png" on screen
pyautogui.sleep(1)
show_password=pyautogui.locateCenterOnScreen("show_password.png",confidence=0.5)
print(show_password)
# Move the mouse cursor to the center of the image and click on it
pyautogui.sleep(1)
pyautogui.moveTo(show_password)
pyautogui.sleep(1)
pyautogui.leftClick()
# Locate the center of the image "password.png" on screen
password=pyautogui.locateCenterOnScreen("password.png",confidence=0.5)
# Move the mouse cursor to the center of the image and click on it
pyautogui.sleep(1)
pyautogui.moveTo(password)
pyautogui.leftClick()
# Use the hotkey combination 'Ctrl + A' to select all text and then use 'Ctrl + C' to copy it
pyautogui.hotkey('ctrl', 'A')
pyautogui.hotkey('ctrl', 'c')
# Wait for a moment and then paste the copied text using pyperclip.paste()
pyautogui.sleep(1)
wifi_password = pyperclip.paste()
pyautogui.sleep(1)
# Close the current window using the hotkey combination 'Alt + F4'
pyautogui.hotkey('alt', 'f4')
pyautogui.hotkey('alt', 'f4')
pyautogui.sleep(1)
pyautogui.hotkey('ctrl', 'w')

pyautogui.sleep(1)

# Open the file in write The Password in wifi_password.txt
with open('wifi_password.txt', 'w') as f:
    # Write the text to the file
    f.write('the wifi password is :'+ wifi_password)