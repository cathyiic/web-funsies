''' 
Spam bot for instagram dms
'''
import pyautogui, time
time.sleep(10)

f = open("document", "r")
for word in f:
  pyautogui.typewrite(word)
  pyautogui.press("enter")


