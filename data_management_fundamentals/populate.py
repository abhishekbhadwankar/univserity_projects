#Student_ID = 21041604
#Task 3a = Design and write a PYTHON script (populate.py) that takes the cleaned CSV file as input and creates a 
#new database instance (pollution-db2) and populates it.

#Importing Pandas and MySql Connector Libraries to perform this task.
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

#Code written in try-except construct as good practice of coding.
try:

#Reading the clean.csv file generated from task 1a. 
    clean_data = pd.read_csv("clean.csv", delimiter =',', keep_default_na = True,low_memory=False)
    
#To establish a connection to the MySQL Workbench
    conn = msql.connect(host='localhost', user='root', passwd="Abhi2021$")
    
#To connect to the MySQL Workbench and create a pollution_db2 database
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS pollution_db2")
        cursor.execute("CREATE DATABASE pollution_db2")
        print("pollution_db2 database is created")
        cursor.execute("use pollution_db2")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
#To create "stations" table in the pollution_db2 databse created above 
        cursor.execute('DROP TABLE IF EXISTS stations;')
        print('Creating table....')
        cursor.execute('''CREATE TABLE pollution_db2.stations( 
        site_id int primary key NOT NULL, 
        location varchar(45) NOT NULL, 
        geo_point_2d varchar(50) DEFAULT NULL
        )''')
        print("\"stations\" table is created....")
        
#Here we are extracting three columns from the dataset that needs to be populated into "stations" table
        station_columns = ['SiteID', 'Location', 'geo_point_2d']
    
#Here we are deleting the duplicates and keeping only the SiteID and Locations that available after cleaning the data in
#in task 1b

        stations = clean_data.drop_duplicates(station_columns)[station_columns]
    
#Here we are iterating through the rows and inserting the data into database. 
        for i, row in stations.iterrows():
            sql = "INSERT INTO pollution_db2.stations (site_id, location, geo_point_2d) VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
        print("Data inserted into \"stations\" table")

#The connection is not autocommitted by default, so we must commit to save our changes
        conn.commit()

#Now, we are creating "station_readings" table into the pollution_db2 database
        cursor.execute('DROP TABLE IF EXISTS station_readings')
        

#Here we are creating the column names and storing it into variable "create_station_readings_table"
#For the columns "nvpm2.5, pm2.5 and vpm2.5" we have replaced the decimal point with "_" 
#as Mysql doesn't recognize decimal values in column names
        create_station_readings_table = '''
            CREATE TABLE pollution_db2.station_readings (
                          reading_id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
                          date_time varchar(40) NOT NULL,
                          nox float DEFAULT NULL,
                          no2 float DEFAULT NULL,
                          no float DEFAULT NULL,
                          pm10 float DEFAULT NULL,
                          nvpm10 float DEFAULT NULL,
                          vpm10 float DEFAULT NULL,
                          nvpm2_5 float DEFAULT NULL,
                          pm2_5 float DEFAULT NULL,
                          vpm2_5 float DEFAULT NULL,
                          co float DEFAULT NULL,
                          o3 float DEFAULT NULL,
                          so2 float DEFAULT NULL,
                          temperature float DEFAULT NULL,
                          rh int DEFAULT NULL,
                          air_pressure int DEFAULT NULL,
                          datestart varchar(40) DEFAULT NULL,
                          dateend varchar(40) DEFAULT NULL,
                          current tinytext,
                          instrument_type varchar(45) DEFAULT NULL,
                          site_id int NOT NULL,
                          PRIMARY KEY (reading_id),
                          KEY site_id_idx (site_id),
                          CONSTRAINT site_id FOREIGN KEY (site_id) REFERENCES pollution_db2.stations (site_id)
                        ) 
        '''

#Here we execute the command to create "station_readings" table in the pollution_db2 database
        cursor.execute(create_station_readings_table)
        print("\"station_readings\" table is created.....")
    
#Here we are selecting the columns from the dataset that must used to populate the data into "station_readings" table
        reading_columns = ['Date Time', 'NOx', 'NO2','NO', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5',
                           'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'DateStart', 
                           'DateEnd', 'Current', 'Instrument Type','SiteID']

#By default pandas will read null/blank values as NaN into the dataframe whereas we want to insert 
#null values in to the station_readings table, hence we have manually converted the NaN values to None

        stations_readings = clean_data[reading_columns].astype(object).where(pd.notnull(clean_data), None)

#Here we are iterating through the rows and inserting the data into database.
        for i, row1 in stations_readings.iterrows():
            sql1 = '''INSERT INTO pollution_db2.station_readings (date_time, nox, no2, no, pm10, nvpm10, vpm10,
            nvpm2_5, pm2_5, vpm2_5, co, o3, so2, temperature, rh, air_pressure, datestart, dateend, current, instrument_type, site_id) 
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
            '''
            cursor.execute(sql1, tuple(row1))
        print("Data inserted into \"station_readings\" table")
        conn.commit()
        
#Now we are creating the lookup table "schema" into the pollution_db2 database
        cursor.execute('''CREATE TABLE pollution_db2.schema(
                measure VARCHAR(15),
                description VARCHAR(100),
                unit VARCHAR(10)
                )''')
        print("\"schema\" table is created")
        cursor.execute('''INSERT INTO pollution_db2.schema(measure,description,unit)
                        VALUES ('Date Time','Date and time of measurement','datetime'),
                        ('NOx','Concentration of oxides of nitrogen','μg/m3'),
                        ('NO2','Concentration of nitrogen dioxide','μg/m3'),
                        ('NO','Concentration of nitric oxide','μg/m3'),
                        ('SiteID','Site ID for the station','integer'),
                        ('PM10','Concentration of particulate matter <10 micron diameter','μg/m3'),
                        ('NVPM10','Concentration of non - volatile particulate matter <10 micron diameter','μg/m3'),
                        ('VPM10','Concentration of volatile particulate matter <10 micron diameter','μg/m3'),
                        ('NVPM2.5','Concentration of non volatile particulate matter <2.5 micron diameter','μg/m3'),
                        ('PM2.5','Concentration of particulate matter <2.5 micron diameter','μg/m3'),
                        ('VPM2.5','Concentration of volatile particulate matter <2.5 micron diameter','μg/m3'),
                        ('CO','Concentration of carbon monoxide','mg/m3'),
                        ('O3','Concentration of ozone','μg/m3'),
                        ('SO2','Concentration of sulphur dioxide','μg/m3'),
                        ('Temperature','Air temperature','°C'),
                        ('RH','Relative Humidity','%'),
                        ('Air Pressure','Air Pressure','mbar'),
                        ('Location','Text description of location','text'),
                        ('geo_point_2d','Latitude and longitude','geo point'),
                        ('DateStart','The date monitoring started','datetime'),
                        ('DateEnd','The date monitoring ended','datetime'),
                        ('Current','Is the monitor currently operating','text'),
                        ('Instrument Type','Classification of the instrument','text')         
                        ''')
        print("Data inserted into \"schema\" table")
        conn.commit()    
        print("All the three tables\"stations, station_readings and schema\" are successfully populated.")
except Error as e:
    print("Error while connecting to MySQL", e)

