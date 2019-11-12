import zipfile
import os

file=zipfile.ZipFile('archive.zip')
print(file.namelist())

sampleinfo=file.getinfo('test0.py')
print(sampleinfo)
print(sampleinfo.file_size)
print(sampleinfo.compress_size)

file.extractall()
file.close()