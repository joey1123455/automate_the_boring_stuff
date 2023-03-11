#! python3
# regexSearch.py - Searches directories for user defined regex exp 

import os,re

#Open a dir and open files with the right extensions
path = os.getcwd()

#Regex engines
extRegex = re.compile(r'^\w+.txt$')     #Find extensions
#User specified regex
print('regex\'s are case sensitive enjoy and re.VERBOSE is active')
regex = input(r'Type a regex expression: ')
userRegex = re.compile(regex, re.VERBOSE)             #Find the user specified regex


for file in os.listdir('C:\\Users\\DELL\\Desktop\\new projects\\python_tutorials\\tic_tac_toe\\prints'):
    #search for correct file extension
    print(file)
    fileName = str(file)
    txtExtension = extRegex.search(fileName)
    #Open individual files
    try:
        txtFile = open(txtExtension.group())
        fileContent = txtFile.read()
        print('original content')
        print(fileContent)
        #Substitute text 
        text = userRegex.sub('**', fileContent)
        print('subbed content')
        print(f'{text}\n')

        
    except:
        print('not .txt\n')
        pass
# print(size)
listOf = os.listdir('C:\\Users\\DELL\\Desktop\\new projects\\python_tutorials\\tic_tac_toe\\prints')
print(listOf)