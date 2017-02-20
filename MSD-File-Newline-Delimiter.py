import re
import sys
import glob
import platform

# If the OS is Windows, the null delimiter may read '\x00' 
if (platform.system()=="Windows"):
	path = "C:/Users/USER/Downloads/VI_LOG/*.TXT"
	files = glob.glob(path)
	for file in files: 
    	JSONdelim = re.sub("\x00|\0", "\n", open(file).read())
    	open(file, "w").write(JSONdelim)
# If the OS is linux-based (e.g. MacOS), the null delimiter will read '\0'
else:
	path = '/Users/USER/Downloads/VI_Log/*.TXT' # SPECIFY PATH TO TRACE FILE(S)   
	files = glob.glob(path)   
	for file in files: 
    	JSONdelim = re.sub("\0", "\n", open(file).read())
    	open(file, "w").write(JSONdelim)