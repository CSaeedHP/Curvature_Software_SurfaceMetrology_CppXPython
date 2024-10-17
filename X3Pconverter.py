

#libraries to read internally
import zipfile
import xmltodict
import hashlib
import struct
# Read the X3P file

'''the following commented out code was used for testing.'''

# my_file = filehandling.OpenFile()

# print(my_file)

# def md5_hash_file(filename):
#     hash_md5 = hashlib.md5()
#     with open(filename, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()

# with zipfile.ZipFile(my_file, 'r') as z:
#     print("data")
#     print(z)
#     with z.open('main.xml') as f:
#             #opens the main.xml file inside
#             content_types = f.read()
#             print(content_types)
#             print("converted")

#             #converting the main.xml into a dictionary, so that you can read the data more easily
#             convertdata = xmltodict.parse(content_types)
#             print(convertdata)
#             #obtain MD5 hash value
#             print("md5 hash")
#             hash = convertdata['p:ISO5436_2']['Record3']['DataLink']['MD5ChecksumPointData']
#             print(hash)

#             file_list = z.namelist()
#             print("Files in the .x3p archive:", file_list)
#             data_bin_path = 'bindata/data.bin'
#             print(data_bin_path)
#             if data_bin_path in file_list:
#                 print("data binary file found!")
#                 with z.open(data_bin_path) as binarydata:
#                     rawpoints = binarydata.read()
#                     hash_md5 = hashlib.md5()
#                     print(rawpoints)

#                     # Assuming binary_data is the raw binary data
#                     # Use len(binary_data) to get the total size in bytes

#                     # Attempt to interpret the binary data as 32-bit floats
#                     num_floats = len(rawpoints) // 8  # Assume 4 bytes per 32-bit float
#                     float_list = list(struct.unpack(f'{num_floats}d', rawpoints))

#                     for chunk in iter(lambda: binarydata.read(4096), b""):
#                         hash_md5.update(chunk)
#                     binaryhashed = hash_md5.hexdigest()



#                     # Print the unpacked floats
#                     print(float_list[:10])
#             else:
#                 print("binary data file not found")
# data = []

# print(len(float_list))
# for i in range(int(len(float_list)/3)):
#     xpoint = float_list[i]
#     zpoint = float_list[i+2]
#     data.append([xpoint, zpoint])
# print(hash)
# print(binaryhashed)
# if hash.lower() ==binaryhashed:
#     print("hash ok")
# else:
#     print("hash error")


#actual function definition starts here.
def readx3p(file_path):
    #final data variable to be returned.

    #read xml as zip archive.
    with zipfile.ZipFile(file_path, 'r') as targetfile:
        #read xml file "main.xml" (this is hardcoded.)
        with targetfile.open('main.xml') as xmldata:
            xmlcontent = xmldata.read()
            #most human readable format, dictionaries within dictionaries
            dictxmlcontent = xmltodict.parse(xmlcontent)
            #grabs hash value from main.xml.
            hash = dictxmlcontent['p:ISO5436_2']['Record3']['DataLink']['MD5ChecksumPointData']
        #reads list of files inside archive
        file_list = targetfile.namelist()
        #hardcoded path for data file.
        data_bin_path = 'bindata/data.bin'
        if data_bin_path in file_list:
            #open the data.bin (a binary file)
            with targetfile.open(data_bin_path) as binarydata:


                #read the raw binary data
                rawpoints = binarydata.read()
                # Assuming binary_data is the raw binary data
                # Use len(binary_data) to get the total size in bytes
                # Attempt to interpret the binary data as 64-bit double
                num_doubles = len(rawpoints) // 8  # Assume 8 bytes per 64-bit double
                #create the list of doubles.
                double_list = list(struct.unpack(f'{num_doubles}d', rawpoints))               

                #hash the file to check for integrity.
                hash_md5 = hashlib.md5()
                for chunk in iter(lambda: binarydata.read(4096), b""):
                    hash_md5.update(chunk)
                binaryhashed = hash_md5.hexdigest()
        else:
            print("no data.bin file found")
    #now that we have our float list, we create the final output
    #int of the length divided by 3, dividing creates float type so we declare it as an int for the range function
    data = []
    for i in range(int(len(double_list)//3)):
        #data is in format x1,y1,z1,x2,y2,z2 so we index the ith and i+2 position, then move to the 3*i and 3*i+2th position
        xpoint = double_list[3*i]
        zpoint = double_list[3*i+2]
        data.append([xpoint, zpoint])
    
    Hashintegritycheck = hash.lower()==binaryhashed
    return data, Hashintegritycheck                               
