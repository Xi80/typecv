import pyautogui
import sys
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
tool = tools[0]
while True:
    txt = tool.image_to_string(pyautogui.screenshot(region = (50,265,850,40)), lang="eng", builder=pyocr.builders.TextBuilder(tesseract_layout=6))
    pyautogui.typewrite(txt,0.01)