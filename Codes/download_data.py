
from bs4 import BeautifulSoup
import requests
import os

# Not needed for now, comment
# point to output directory

try:
    os.system('mkdir -p ../Data/Raw/Zips')
except OSError as err:
    print('OS error: {0}'.format(err))



outpath = '../Data/Raw/Zips/'
url = 'https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=f3c0f7d512273410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default'
mbyte=1024*1024

print( 'Reading: ', url[0:30], '...')
html = requests.get(url).text
soup = BeautifulSoup(html, features = 'lxml')

print ('Processing: ', url[0:30], '...')
for name in soup.findAll('a', href=True):
    zipurl = name['href']
    if( zipurl.endswith('.zip') ):
        outfname = outpath + zipurl.split('/')[-1]
        zipurl = 'https://datos.madrid.es' + zipurl
        print(zipurl)
        r = requests.get(zipurl, stream=True)
#        print(r.status_code)
#        print(r.headers)
        if( r.status_code == requests.codes.ok ) :
#            fsize = int(r.headers['content-length'])
#            print ('Downloading %s (%sMb)' % ( outfname, fsize/mbyte ))
            with open(outfname, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1024): # chuck size can be larger
                    if chunk: # ignore keep-alive requests
                        fd.write(chunk)
                fd.close()

############## This worked! Let's commit it


dataraw = '../Data/Raw/'
# Unzipping everything
#os.system('unzip ../Data/Zips/\*.zip -d ../Data/')
os.system('unzip ' + outpath + '/\*.zip -d ' + dataraw)

# Renaming the folders that were created when unzipping
for i in range(3,10):
    os.system('mv ' + dataraw + 'Aдo0' + str(i) + '/ ' + dataraw + 'Year200' + str(i) + '/')
for i in range(0,2):
    os.system('mv ' + dataraw + 'Aдo1' + str(i) + '/ ' + dataraw + 'Year201' + str(i) + '/')

# Creating the folders that were not created when unzipping
for i in range(12,22):
    os.system('mkdir ' + dataraw + 'Year20' + str(i) + '/')
for i in range(1,3):
    os.system('mkdir ' + dataraw + 'Year200' + str(i) + '/')


# Gathering all file names of the folder Data
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(dataraw) if isfile(join(dataraw, f))]

# Gathering those data files that were not unzipped into a folder and 
# moving them into a folder
formats = ['txt', 'csv', 'xml']
for f in onlyfiles:
    if any(frmt in f for frmt in formats):
#        print(f)
        for i in range(0,22):
            if i < 10:
                if '0'+str(i) in f:
                    os.system('mv ' + dataraw + f +' ' + dataraw + 'Year200' + str(i) + '/' + f)
            else:        
                if str(i) in f:
                    os.system('mv ' + dataraw + f +' ' + dataraw + 'Year20'  + str(i) + '/' + f)
            
# Standardize the names of the data files MM-YYYY.format
months = {'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04',
          'may': '05', 'jun': '06', 'jul': '07', 'ago': '08',
          'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'}

# loop through years
for i in range(1,22):
    # case of 2001 to 2009
    if i < 10:
        mypath = '../Data/Raw/Year200' + str(i)
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        # loop through months
        for mo in months.keys():
            # loop through files in mypath
            for f in onlyfiles:
                if mo in f.lower():
                    os.system('mv ' + mypath + '/' + f + ' ' + mypath +
                                    '/' + months[mo] + '-' + '200' + str(i) + f[-4:])
    else:
        mypath = '../Data/Raw/Year20' + str(i)
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for mo in months.keys():
            for f in onlyfiles:
                if mo in f.lower():
                    os.system('mv ' + mypath + '/' + f + ' ' + mypath +
                                    '/' + months[mo] + '-' + '20' + str(i) + f[-4:])

        

#os.system('mv ..Data\*')
