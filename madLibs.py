#! python3
# madLibs.py - Reads text documents for keywords and creates new documents

import os, re

#Regex engines.
adjectiveRegex = re.compile(r'adjective', re.I)    #Finds the word adjective
verbRegex = re.compile(r'verb', re.I)     #Finds the word verb
nounRegex = re.compile(r'noun', re.I)     #Finds the word noun
adverbRegex = re.compile(r'adverb', re.I)       #Finds the word adverb

#Open and read a .txt file.
txtFile = open('madlibstest.txt')
txtContent = txtFile.read()
# print(txtContent)

#Replacing matches with user input
text = txtContent

slot = adjectiveRegex.search(text)
if slot != None: 
    adjective = input('Please type an adjective: ').lower()
    text = adjectiveRegex.sub(adjective, text)
slot = nounRegex.search(text)
if slot != None:    
    noun = input('Pleas type a noun: ').title()
    text = nounRegex.sub(noun, text)
slot = adverbRegex.search(text)
if slot != None:
    adverb = input('Please type an adverb: ').lower()
    text = adverbRegex.sub(adverb, text)
slot = verbRegex.search(text)
if slot != None:    
    verb = input('Please type a verb: ').lower()
    text = verbRegex.sub(verb, text)
print(text)

#Write a new file
newFile = open('madlibstestresults.txt', 'a')
newFile.write('\n')
newFile.write(f'{text}\n')
