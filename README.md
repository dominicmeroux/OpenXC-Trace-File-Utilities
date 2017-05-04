# MSD-File-Newline-Delimiter

Removes the null escape character and adds a newline delimiter. This program is designed for OpenXC trace files written to an SD card with a null delimiter (e.g. as opposed to trace files recorded by the Enabler app, which adds a newline delimiter).    

# MSD-File-Newline-Delimiter-Subdirectories

Does the same thing as the first file, but looks at files in all subdirectories. 

NOTE: Run time on a Windows 10 desktop computer with 16GB RAM was about 7 minutes for ~13.5 GB of trace files

# OpenXC_trace_to_csv

Converts drive trace files from JSON format to CSV format with specified variables

Using PySpark version 1.6.1 and Python 2.7.12 :: Anaconda custom (x86_64)

Before using the code, you must either obtain a JSON drive trace file from the OpenXC web site (http://openxcplatform.com/resources/traces.html), or generate your own JSON trace files using a Reference VI. 

This is initial work on using PySpark to work with OpenXC drive trace data, in this case converting an OpenXC JSON drive trace to a CSV file. 
