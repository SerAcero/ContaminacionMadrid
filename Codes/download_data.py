
from bs4 import BeautifulSoup
import requests

# point to output directory
outpath = '../Data/'
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

# This worked! Let's commit it

