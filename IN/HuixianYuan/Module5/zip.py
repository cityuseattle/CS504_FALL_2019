import zipfile

newzip=zipfile.ZipFile('archive.zip','w')
newzip.write('test0.py', compress_type=zipfile.ZIP_DEFLATED)
newzip.close()

newzip=zipfile.ZipFile('archive.zip', 'a')
newzip.write('test3.py', compress_type=zipfile.ZIP_DEFLATED)
newzip.close()

newzip=zipfile.ZipFile('archive.zip','a')
newzip.write('test4.py',compress_type=zipfile.ZIP_DEFLATED)
newzip.close()