#! python3
# bankDetailsSensor - Sensors bank details from text

import re, pyperclip

#Regex engines 
cardNoRegex = re.compile(r'''
(
   (\d{4})      #4 digits
   ([-,. ])?    #Seperator
   (\d{4})      #4 digits2
   ([-,.\s])?    #Seperator
   (\d{4})      #4 digits3
   ([-,.\s])?    #Seperator
   (\d{4})      #4 digits4
)''', re.VERBOSE)

cvvRegex = re.compile(r'\d{3}')

accNoRegex = re.compile(r'\d{10}')

expiryDate = re.compile(r'(\d\d?)([- :])?(\d\d?)')

#Input
text = 'these are my cardno\'s 1234345567894567, 3456-3456-3444-7900 3444,5667,8907,4565 3333-3333-3333-3333 4444 4444 4444 4444 and my cvv is 234, 234, 555 576 these are my expiry dates 11/22, 5/23, 12/2, 12/02 and my accno is 1234567891'
# text = pyperclip.paste()

#Censor details
censoredCvv = cvvRegex.sub('***', text)
censoredCvv = str(censoredCvv)
censoredCardNo = cardNoRegex.sub('**********', censoredCvv)
censoredExpiryDate = expiryDate.sub('**', censoredCardNo)
censoredAccNo = accNoRegex.sub('**********', censoredExpiryDate)

#Output string
print(censoredAccNo)
pyperclip.copy(censoredAccNo)