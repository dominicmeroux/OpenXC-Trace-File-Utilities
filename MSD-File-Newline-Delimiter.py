import re
import sys
import glob

path = '/Users/USER/Downloads/VI_Log/*.TXT' # SPECIFY PATH TO TRACE FILE(S)   
files=glob.glob(path)   
for file in files: 
    JSONdelim = re.sub("\0", "\n", open(file).read())
    open(file, "w").write(JSONdelim)
