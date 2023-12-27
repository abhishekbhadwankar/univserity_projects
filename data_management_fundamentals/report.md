**Task 6: Reflective Report** 

I have read the assignment and understood that the dataset Bristol Air Quality has the data of air quality measured for various air pollutants such as Nitrogen Monoxide (NO),Nitrogen Dioxide (NO2) and particulate matters. This dataset is huge with data collected from 2004 to 2021 measured across 18 stations in Bristol.

The next step, I did was to download the bristol-air-quality-data.zip and opened it in Notepad++ as MS Excel was not able to handle this huge data. I briefly tried to understand the data before performing the tasks.

**My approach for solving the task 1A** :

1. My Understanding of the Requirements:
  - To take Bristol Air Quality csv file and delete the data before "1 Jan 2010" in Python. The output        should a be a crop.csv which has 744743 lines.

2. I have used Pandas Library in Python to read the original file and then filter the data based on date more than "2010" without doing any datatype change or the data.

3. Transferred the filtered data to create a new crop.csv file using pandas commands.


**Reason for using this approach** :

Initially, I changed the date format and then did the filter. However, later I learned that without changing the date format we can still filter the data, hence by doing this I kept the code simple and straight forward.

**My approach for solving the task 1B** :

1. My Understanding of the Requirements:
  - To take the crop.csv file generated from task 1a and delete the mismatches between SiteID and Location and where there are no values for SiteID.

2. I have again used Pandas Library for this task and read the crop.csv file and constructed a code that will check the mismatches and Null values and stores the Index numbers in a variable to print number of lines that are mismatched. 

3. Deleted the mismatch values stored in the variable and transferred the data into clean.csv file that has 743995 lines in it.

**Reason for using this approach** :

Familiarity with Pandas Library.


**My approach for  solving the task 2** :

1.  My Understanding of the Requirements:
  - Using MySQL Workbench we have to create Entity-Relationship diagram in 3N form and using forward engineering feature create a blank database that has the tables.

2.  The first step I did for modelling is to find the Entities and the attributes. Based on the data relationship, I divided into three entities and the respective attributes:
  - Station: that has attributes, SiteID, Location and geo_point_2d.
  - Station_Readings: that has all the other remaining attributes.
  - Schema: this is basically a lookup table that has all the schema information such as measure, description and units. 
  
3.  Then, I created ER diagram in MySQL workbench.

4.  In MySQL workbench using forward engineer feature, the ER model was transformed into database that has entities in tables and the attributes as column names within each entity.

5.  Using export option in MySQL, the syntax of the database created using above steps is transferred to SQL file. 


**My approach for  solving the task 3A** :

1. My Understanding of the Requirements:
  - We have to take the clean.csv file generated from task 1b and design a python script that would create three tables station, station_readings and schema in the MySQL in separate database pollution-db2.

2. I have used Pandas and mysql.connector libraries for this task, as I'm familiar with using Pandas and mysql.connector to connect to MySQL workbench.

3. Then designed a python script to  perform the following instructions:
  - Connect and create "pollution-db2" database in MySQL.
  - Create "stations" table that has three column 'SiteID', 'Location' and 'geo_point_2d' and insert values from the csv file.
  - Create "station_readings" table that has remaining columns and insert values into it from the csv file.
  - Create "schema" table and manually insert values into it.
4. I have added print command at the end of the script that would confirm if all the data is transferred successfully.

**Reason for using this approach** :

After all the different possibilities, I found that this approach was well structured and in a sequence that gave me more understanding of handling data and populating data in the database without much of issues. 

**My approach of solving the task 3B** :

1. My Understanding of the Requirements:
  - Initially, I found it very difficult to understand the requirement and how to perform this task. However, after clarification from Professor I was able to design python script that would generate a SQL file that holds insert statement for the first 100 records.

2. I have used Pandas and datetime libraries for this task and the Clean.csv file. Here, using Pandas function "nrows = 100" I was able to select 100 rows from the big clean.csv file.

3. Then designed a python script to  perform the following instructions:
  - To open "insert-100.sql" in  write mode.
  - Then using "for loop" iterate through the rows and generate insert file.
  - The close the "insert-100.sql" file after sucessful creation.

**Reason for using this approach** :

As this task was difficult for me to understand, hence I could find only the above approach to perform this task.


**My approach of solving the task 4** :

The three SQL queries provided a very useful output but were challenging to execute. In the first query I learned about how to perform "INNER JOIN" to get information from table. While displaying the output table, I tried to round values neatly to two decimal places and also renamed columns clearly for an user to understand well. 

In the second query, it is asked to take readings on or near 8:00 hours which is peak time intensity. I noticed that the readings are hourly, therefore I gave condition using "WHERE" the time is equal to 08:00:00 hours. 

Third query was just an extension of the second query, where we had to show values for all stations in the years 2010 to 2019. With the use "BETWEEN" condition I was able to select values between 2010 and 2019. 

**My approach of solving the task 5** :

The task was to model data in NoSQL database. Unfortunately, could not learn much on the NoSQL before but was able to cope up with the online tutorials. After going through all the available NoSQL databases, I selected Key-value data model in JASON format in MongoDB. 

With the help of online materials, I was able to successfully create a database in MongoDB and enter the data into it.
 
**Visualization of the data** 

 Python Seaborn Library helps in plotting data using different color schemes and extending to find a regressing model fit.
 
1. Using PalPlot() we can display color palettes for the pollutants level ranging from safe to harmful.
 
2. Using LinePlot() we can show line graphs stating trend measurements of different pollutants in a timeline.
 
3. Using ScatterPlot() we can display a trend of different pollutants when they are highly active during the peak times.

**Summary** 

Overall, the assignment was very challenging and that gave glimpse of understanding data, data cleaning, cropping and transferring data into a database and finally an introduction to NoSQL database.  
Along the journey, I also learnt better ways to design schema and improved well upon defining proper referential integrity constraints.
