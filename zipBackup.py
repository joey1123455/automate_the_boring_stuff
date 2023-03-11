#! python3
# zipBackup.py - Backs up file data as a versioned zip file

import zipfile, os

def zipBackup(folder):
    #Back up entire contents of folder
    folder = os.path.abspath(folder)        #Makes sure folder is absolute

    #Figure out what filename this code should use based on what files already exist
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1
    
    #Create the ZIP file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    #Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #Add the current folder to the zip file
        backupZip.write(foldername)
        #Add all the files in this folder to the zip file
        for fileName in filenames:
            newBase / os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue    #Don't backup the backup Zip files
            backupZip.write(os.path.join(foldername, fileName))
    backupZip.close()
    print('Done')
zipBackup('C\\delicious') 