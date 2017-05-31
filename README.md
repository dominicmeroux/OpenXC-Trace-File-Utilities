# MSD-File-Newline-Delimiter

Removes the null escape character and adds a newline delimiter. This program is designed for OpenXC trace files written to an SD card with a null delimiter (e.g. as opposed to trace files recorded by the Enabler app, which adds a newline delimiter).    

# MSD-File-Newline-Delimiter-Subdirectories

Does the same thing as the first file, but looks at files in all subdirectories. 

NOTE: Run time on a Windows 10 desktop computer with 16GB RAM was about 7 minutes for ~13.5 GB of trace files

# Azure-Webserver-MSSQL-Data-Cleaner.cs

If you set up the (OpenXC Azure Webserver)[https://github.com/openxc/openxc-azure-webserver] to read streaming data from a C5 Cellular VI, this data cleaner CSharp program reads in all data from your database and reformats the data to paste together partial messages and add a newline delimiter. This reformatted version is easier to read in data analysis software, for example as a table in Databricks PySpark. 

An example of the raw data from the MS SQL server: 

`{"records":[ng_wheel_angle","value":281.500000},{"timestamp":1496024469947,"name":"headlamp_status","value":false},`

An example of the reformatted data:

`{"timestamp":1496172206206,"name":"torque_at_transmission","value":-500},
{"timestamp":1496172206337,"name":"brake_pedal_status","value":"false"},
{"timestamp":1496172206338,"name":"fuel_consumed_since_restart","value":4.672964},`

# OpenXC_trace_to_csv

Converts drive trace files from JSON format to CSV format with specified variables

Using PySpark version 1.6.1 and Python 2.7.12 :: Anaconda custom (x86_64)

Before using the code, you must either obtain a JSON drive trace file from the OpenXC web site (http://openxcplatform.com/resources/traces.html), or generate your own JSON trace files using a Reference VI. 

This is initial work on using PySpark to work with OpenXC drive trace data, in this case converting an OpenXC JSON drive trace to a CSV file. 
