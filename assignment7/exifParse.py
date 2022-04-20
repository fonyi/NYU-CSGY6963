#!/usr/bin/python3
import os
import sys
#import exifread
from exif import Image
#import piexif

#Read in exactly 1 argument
if len(sys.argv) == 2:
    image_file = sys.argv[1]
else:
    print('Error! - No Image File Specified!')
    exit()

#Check if file exists and assign
try:
    with open(image_file, 'rb') as f:
        image = Image(f)
except OSError:
    print('Error! - File Not Found!')
    exit()


print('Source File: '+sys.argv[1])
print('Make: '+image.make)
print('Model: '+image.model)
print('Original Date/Time: '+image.datetime)
print('Latitude: '+str(int(image.gps_latitude[0]))+' degrees, '+str(image.gps_latitude[1])+' minutes, '+str(image.gps_latitude[2])+' seconds')
print('Longitude: '+str(int(image.gps_longitude[0]))+' degrees, '+str(float(image.gps_longitude[1]))+' minutes, '+str(float(image.gps_longitude[2]))+' seconds')
