#HEIC to JPG image format batch conversion script for Python 3. Tested on Windows 10.
#You will need to have ImageMagick installed: https://www.imagemagick.org/

import os, subprocess


##Input and Output Variables
directory = '../heic'
outputDirectory = '../output'
######

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"): 
        print('Converting %s...' % os.path.join(directory, filename))
        fullName = os.path.join(directory, filename)
        subprocess.run(["magick", "%s" % fullName, "%s" % (outputDirectory+filename[0:-5] + '.jpg')])
        continue
