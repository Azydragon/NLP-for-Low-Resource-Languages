import re
text=("Hello!, I am building my first project.")
text=text.lower()
clean_text=re.sub(r'[^\w\s]','',text)
tokens=clean_text.split()
print(tokens)
