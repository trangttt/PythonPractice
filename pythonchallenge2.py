import re

file = open("ocr.html").read()

re.findall(r'<!--(.*)-->', file)
