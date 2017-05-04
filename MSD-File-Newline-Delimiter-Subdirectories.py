import re
import os
import sys
import glob
import platform

# If the OS is Windows, the null delimiter may read '\x00' 
if (platform.system()=="Windows"):
	path = "D:/DRIVE_TRACES/"
	for root,dirs,filenames in os.walk(path):
		for file in filenames:
			#print file
			# If this is a text file, make the changes
			if ((re.match( r'........\.TXT', file))):
				# take care of case where there are two backslashes
				#print root+file
				Final_File = re.sub(r'\\', '/', (root+"/"+file))
				#print re.sub(r'\\', '/', re.sub(r'\\', '/', (root+file)))
				JSONdelim = re.sub("\x00|\0", "\n", open(Final_File).read())
				open(Final_File, "w").write(JSONdelim)