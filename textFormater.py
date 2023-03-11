#! python3
#textFormater.py - Formats texts from clipboard

import pyperclip,re

#Regex engines
exclamationRegex = re.compile(r'''
(
    (!+)    #exclamation marks
)''', re.VERBOSE)

multiSpaceRegex = re.compile(r'([  ]+)')

#Todo repeated words regex engine
# reptWordsRegex = re.compile(r'^[]')   # (^\w$)?      #repetedwords

text = pyperclip.paste()

matches = exclamationRegex.sub('!', text)
matches2 = multiSpaceRegex.sub(' ', matches)
# matches3 = reptWordsRegex.sub('extra', text)

pyperclip.copy(matches2)
    # print('append')
# print('appnd')
# print(matches)
print(matches2)
print('testing...')
# print(matches3)
# if len(matches) > 0:
#     quantity = len(matches)
#     print(quantity)
#     string = ' -'.join(matches)
#     print(str(string))
# else: 
#     print('none')

