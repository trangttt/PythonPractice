import re

def is_alphabetized(text):
    lower_text = text.lower()
    text = re.sub(r'[^a-z]','', lower_text)
    return "".join(sorted(text)) == text
