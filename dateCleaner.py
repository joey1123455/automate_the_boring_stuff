#! python3
# dateCleaner.py - Cleans out dates from text

import re, pyperclip

#Regex engine
dateRegex = re.compile(r'''
(
    (\d+)           #First digits
    ([-,_;:/.|])?      #Seperators
    (\d+)           #Second digits
    ([-,_;:/.|])?      #Seperators
    (\d+)           #Last digits
    
)''', re.VERBOSE)

#Stringify into prefered format
text = pyperclip.paste()
matches = []
for groups in dateRegex.findall(text):
    date = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(date)

#Print dates
if len(matches) > 0:
    strng = '\n'.join(matches)
    print('ran')
    pyperclip.copy(strng)
    print(strng)
else:
    print('none')
