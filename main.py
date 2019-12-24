import pyautogui
import sys
import pyocr.builders
tools = pyocr.get_available_tools()
tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]
tool = tools[0]
while True:
    txt = tool.image_to_string(pyautogui.screenshot(region = (50,265,850,40)), lang="eng", builder=pyocr.builders.TextBuilder(tesseract_layout=6))
    pyautogui.typewrite(txt,0.01)
