#! python3
# urlRegex.py - Find emails starting with https:// or https://

import pyperclip, re

#Regex engine
emailRegex = re.compile(r'''
(
    (https?://)                      #Connection cert
    (www)?                                  #www
    (\.)?                                   #.
    (\w+)                                    #Domain name
    (\.)                                    #. 
    (([a-zA-Z/]+)(\.)?([a-zA-Z/]+)?)   #Domain
)''', re.VERBOSE)

#Text from clipboard
text = pyperclip.paste()

#Sort through the text
matches = []
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Stringify matches
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print(matches)
else:
    print('No urls')