#Student_ID = 21041604
#Task 3a = Create a PYTHON script (insert-100.py) that generates a SQL file (insert-100.sql) 
#that holds the first 100 inserts to the readings table.

#Importing Pandas and datetime Libraries to perform this task.
import pandas as pd
from datetime import datetime

#Code written in try-except construct as good practice of coding.
try:
#Reading the clean.csv file generated from task 1a and selecting first 100 rows using "nrows=100"    
    clean_data = pd.read_csv("clean.csv", delimiter =',', nrows=100)

#Here we are selecting the columns from the dataset that must used to populate the data into "station_readings" table
    reading_columns = ['Date Time', 'NOx', 'NO2','NO', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5',
                   'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'DateStart', 
                   'DateEnd', 'Current', 'Instrument Type','SiteID']

# In the following string, we create the sql insert statement, with placeholders for column namesand values. 
#{0} is for columns and {1} is for values

    insertSQL = "INSERT INTO `pollution_db`.station_readings ({0}) VALUES ({1})"
    
# We enclose column names with backtick(`) so that the column names can be used as it is while
# inserting the data into the table
    field_names = ",".join(["`{0}`".format(x) for x in reading_columns])
    
# Reading only required columns from the dataframe
    stations_readings = clean_data[reading_columns]

#To open "insert-100.sql" file to hold the first 100 inserts
    createOnFile = open("insert-100.sql","w+")
    
#While forming the insert statement string and datetype column values should be enclosed within
#single quotes. So we use the following code to achieve the required formatting.
#We determine value is of type string or datetime with the help of the python's built in
#"isinstance" method and enclose the values within in single quotes.Other values will not be enclosed within single quotes(') 

#We then iterate through the rows and generate insert file.
    for i, row in stations_readings.iterrows():
        value_list = row.values
        for pos, value in enumerate(value_list):
            if isinstance(value, str):
                value_list[pos] = "'{0}'".format(value)
            elif isinstance(value, datetime):
                value_list[pos] = "'{0}'".format(value.strftime('%Y-%m-%d'))

        values = ','.join(str(v) for v in value_list)
        sql = insertSQL.format(field_names, values).replace('nan','')
        createOnFile.write(sql + "\n")
    createOnFile.close()
    print("insert-101.sql file created successfully")
    
except Error as e:
    print("Error while connecting to MySQL", e)

