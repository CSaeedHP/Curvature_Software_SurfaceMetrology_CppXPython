import pandas as pd
import x3p
from x3p import X3Pfile
import filehandling


#libraries to read internally
import zipfile
import xml.etree.ElementTree as ET
import numpy as np
import xmltodict
import os
import hashlib
# Read the X3P file
my_file = filehandling.OpenFile()
print(my_file)

def md5_hash_file(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

with zipfile.ZipFile(my_file, 'r') as z:
    print("data")
    print(z)
    with z.open('main.xml') as f:
            #opens the main.xml file inside
            content_types = f.read()
            print(content_types)
            print("converted")

            #converting the main.xml into a dictionary, so that you can read the data more easily
            convertdata = xmltodict.parse(content_types)
            print(convertdata)
            #obtain MD5 hash value
            print("md5 hash")
            hash = convertdata['p:ISO5436_2']['Record3']['DataLink']['MD5ChecksumPointData']
            print(hash)

            file_list = z.namelist()
            print("Files in the .x3p archive:", file_list)
            data_bin_path = 'bindata/data.bin'
            print(data_bin_path)
            if data_bin_path in file_list:
                print("data binary file found!")
                with z.open(data_bin_path) as binarydata:
                    hash_md5 = hashlib.md5()
                    for chunk in iter(lambda: binarydata.read(4096), b""):
                        hash_md5.update(chunk)
                    binaryhashed = hash_md5.hexdigest()
                    rawpoints = binarydata.read()

                    print(rawpoints)
                    import struct

                    # Assuming binary_data is the raw binary data
                    # Use len(binary_data) to get the total size in bytes

                    # Attempt to interpret the binary data as 32-bit floats
                    num_floats = len(rawpoints) // 8  # Assume 4 bytes per 32-bit float
                    float_list = list(struct.unpack(f'{num_floats}d', rawpoints))

                    # Print the unpacked floats
                    print(float_list[:10])
            else:
                print("binary data file not found")
data = []

print(len(float_list))
for i in range(int(len(float_list)/3)):
    xpoint = float_list[i]
    zpoint = float_list[i+2]
    data.append([xpoint, zpoint])
print(hash)
print(binaryhashed)
if hash.lower() ==binaryhashed:
    print("hash ok")
else:
    print("hash error")