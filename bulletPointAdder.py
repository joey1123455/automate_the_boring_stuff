#! python3
# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text on clipboard.add()

import pyperclip
text = pyperclip.paste()
#seprate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = f'* {lines[i]}' #add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)

# bulletPoint = pyperclip.paste()
# print(bulletPoint)