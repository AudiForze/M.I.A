import pyautogui


def scroll_up():
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')


def scroll_down():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')

def scroll_to_top():
    pyautogui.hotkey('home')

def scroll_to_bottom():
    pyautogui.hotkey('end')
