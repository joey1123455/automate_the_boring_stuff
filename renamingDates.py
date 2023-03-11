#! python3
# renamingDates.py - Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import shutil, os, re

#Create a regex that matches files with American date format.
#Regex engine
dateRegex = re.compile(r'''
    ^(.*?)              #All text before the date
    ((0|1)?\d)-         #One or two digits for month
    ((0|1|2|3)?\d)-     #One or two digits for the month
    ((19|20)\d\d)       #Four digits for the year
    (.*?)$              #All text after the date
''', re.VERBOSE)        

#Loop over files in working directory
for americanFileName in os.listdir('.'):
    mo = dateRegex.search(americanFileName)

    #Skip files without a date.
    if mo == None:
        continue

    #Get the diffrent parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #Form the european style filename
    euroFileName = f'{beforePart}{dayPart}-{monthPart}-{yearPart}'

    #Get the full, absolute file path
    absWorDir = os.path.abspath('.')
    americanFileName = os.path.join(absWorDir, americanFileName)
    euroFileName = os.path.join(absWorDir, euroFileName)

    #Rename the files
    print('Renaming "%s" to "%s"...' % (americanFileName, euroFileName))
    shutil.move(americanFileName, euroFileName)