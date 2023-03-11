#! python3
# madLibs.py - Reads text documents for keywords and creates new documents

import os, re

#Regex engines.
adjectiveRegex = re.compile(r'adjective', re.I)    #Finds the word adjective
verbRegex = re.compile(r'verb', re.I)     #Finds the word verb
nounRegex = re.compile(r'noun', re.I)     #Finds the word noun
adverbRegex = re.compile(r'adverb', re.I)       #Finds the word adverb
regexEngines = [nounRegex, adjectiveRegex, adverbRegex, verbRegex]      #List of regex engines.

#Individual regex substitue functions
def adverbRegSub(text):
    #Accept input and substitute text data   
    adverb = input('Please type an adverb: ').lower()
    sub = adverbRegex.sub(adverb, text)
    return sub
def adjectiveRegexSub(text):
    #Accept input and substitute text data   
    adjective = input('Please type an adjective: ').lower()
    text = adjectiveRegex.sub(adjective, text)
    return text
def nounRegexSub(text):  
    #Accept input and substitute text data   
    noun = input('Pleas type a noun: ').title()
    text = nounRegex.sub(noun, text)
    return text
def verbRegexSub(text): 
    #Accept input and substitute text data   
    verb = input('Please type a verb: ').lower()
    text = verbRegex.sub(verb, text)
    return text

#Select regex sub function
def regexSubstitue(text,slot):
    #Matches items in regex engine list to keywords and selects substitution function
    cont = text
    sub = ''
    if slot == 'adverb':
        adverbRegSub(cont)
        sub = sub
        print(sub)
    elif slot == 'adjective':
        adjectiveRegexSub(cont)
    elif slot == 'verb':
        verbRegexSub(cont)
    elif slot == 'noun':
        nounRegexSub(cont)
    else: 
        print(text)
    print(cont)



#Open and read a .txt file.
txtFile = open('madlibstest.txt')
txtContent = txtFile.read()

#Replacing matches with user input
text = txtContent
for engine in range(len(regexEngines)):
    #sorts out regex engines to use if found in file
    slot = regexEngines[engine].search(text)
    slot = slot.group().lower()
    if slot != None:
        # print(slot)
        regexSubstitue(text,slot)
print(text)

#Write a new file
# newFile = open('madlibstestresults.txt', 'a')
# newFile.write('\n')
# newFile.write(f'{text}\n')
