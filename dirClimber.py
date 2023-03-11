import os

for folderName, subFolders, fileNames in os.walk('C:\\delicious'):
    print(f'The current folder is {folderName}')

    for subFolder in subFolders:
        print(f'SUBFOLDER OF {folderName}: {subFolder}')
    
    for fileName in fileNames:
        print(f'FILE INSIDE: {folderName}: {fileName}')

    print(' ')