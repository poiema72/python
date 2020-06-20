from optparse import OptionParser
import zipfile
import sys

from bs4 import BeautifulSoup

# option = OptionParser(usage='%prog', version='%prog 0.1')

# (option, args) = option.parse_args()

TIZEN_TPK = 'tizen-manifest.xml'
TIZEN_WGT = 'config.xml'

with zipfile.ZipFile(sys.argv[1]) as tizen_pkg:
    print(sys.argv[1])
    if TIZEN_TPK in tizen_pkg.namelist():
        with tizen_pkg.open(TIZEN_TPK) as tizen_manifest:   
            soup = BeautifulSoup(tizen_manifest, "html.parser")
            for element in soup.find_all('ui-application'):
                print('Native app')
    elif TIZEN_WGT in tizen_pkg.namelist():
        print("Web app")
    else:
        print("Error: Unknown type of package")

