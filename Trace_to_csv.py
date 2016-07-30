import pandas

# store filename and path in variable "filename"
filename = "MY-OPENXC-DRIVE-TRACE-FILENAME.json"

# read into dataframe
testJsonData = sqlContext.read.format('json').load(filename)

# register dataframe as a table
sqlContext.registerDataFrameAsTable(testJsonData, "table1")

### this example extracts engine speed and transmission gear position...use the general approach to extract any desired variable
engine_speed = sqlContext.sql("SELECT timestamp, DOUBLE(value) as engine_speed FROM table1 WHERE name = 'engine_speed'")

transmission_gear_position = sqlContext.sql("SELECT timestamp as timestamp2, value as transmission_gear_position FROM table1 WHERE name = 'transmission_gear_position'")

# the two variables are joined by timestamp
Shifting = engine_speed.join(transmission_gear_position, engine_speed.timestamp == transmission_gear_position.timestamp2, "inner")

# use Pandas to write the file to a local csv file
output_file = 'MY-OUTPUT-CSV-FILE.csv'
Shifting.toPandas().to_csv(output_file)

# alternatively, use spark-csv
# 
# if taking this approach and using a version of PySpark that differs from 1.6.1, 
# refer to http://stackoverflow.com/questions/31385363/how-to-export-a-table-dataframe-in-pyspark-to-csv
# to determine the syntax that will be needed
Shifting.write.format('com.databricks.spark.csv').save(output_file) 