**Database** : MongoDB

**Data Model** : key-value

**Task 5 : Model the data for a specific monitor (station) to a NoSQL data model**

**Background Research about NoSQL Database,**

1. I did research to understand what are NoSQL Databases and its advantages over Relational Database Management System (RDBMS).

2. The RDBMS requires data to be normalized into tables that are composed of rows and columns, whereas NoSQL databases can be modelled into key-value, documents and graph based data models that offer better performance and scalability.

3.  The major advantages of NoSQL database over RDBMS is:
    - Flexibility
    - Scalability
    - High-performance
    - Highly functional.
4. Among the various NoSQL databases available, I have chosen MongoDB database to perform this task as it is one of most popular and user friendly document based database.

5. Basic difference between SQL vs. NoSQL Terminology:


       | SQL         | NOSQL       |
       | ----------- | ----------- |
       | Table       | Collection  |
       | Row         | Document    |
       | Column      | Field       |
       | Primary key | ObjectID    |
       
     
   
**Setting up MongoDB database**

1. Installed MongoDB Community Server (Ver. 5.0.5) locally onto the system from [https://www.mongodb.com/try/download/community]

2. Installed MongoDB Compass GUI for MongoDB. This was installed along with Community Server package.

3. To Start and verify if MongoDB is installed correctly: Open the command prompt and type "mongod" and then open one more command prompt window and type "mongo".

**Data Modelling in  MongoDB database and populating data**

1. I have selected 5 records of Station "AURN St Pauls" (SiteID = 452) from the original "bristol-air-quality-data.csv" to model the data in MongoDB.

2. Manually entered 5 records in key-value format through Command Line into MongoDB for Station "AURN St Pauls" (SiteID = 452).

3. Renamed the keys (nvpm2.5, pm2.5, vpm2.5) which are having a Full point in the name, because NoSQL database does not accept full point in the key.

**Script for populating data into MongoDB database**
```
> use pollution_db

> db.createCollection("bristol_air_quality_data")

> db.bristol_air_quality_data.insertMany([{
... Date_Time : new Date("2020-11-05T19:00:00+00:00"),
... Nox : 264.881,
... No2 : 65.025,
... No : 130.343,
... SiteID : 452,
... PM10 : 86.958,
... NVPM10 : "NULL",
... VPM10 : "NULL",
... NVPM2_5: "NULL",
... PM2_5: 62,
... VPM2_5: "NULL",
... CO: "NULL",
... O3: 2.994,
... SO2: "NULL",
... Temperature: "NULL",
... RH: "NULL",
... Air_Pressure: "NULL",
... Location: "AURN St Pauls",
... geo_point_2d: "51.4628294172,-2.58454081635",
... DateStart: new Date("2006-06-15T00:00:00+00:00"),
... DateEnd: "NULL",
... Current: "TRUE",
... Instrument_Type: "Continuous (Reference)"},
... {
... Date_Time : new Date("2020-01-01T00:00:00+00:00"),
... Nox : 29.037,
... No2 : 27.1229,
... No : 1.2484,
... SiteID : 452,
... PM10 : 44.445,
... NVPM10 : "NULL",
... VPM10 : "NULL",
... NVPM2_5: "NULL",
... PM2_5: 40,
... VPM2_5: "NULL",
... CO: "NULL",
... O3: "NULL",
... SO2: "NULL",
... Temperature: 3.3,
... RH: "NULL",
... Air_Pressure: "NULL",
... Location: "AURN St Pauls",
... geo_point_2d: "51.4628294172,-2.58454081635",
... DateStart: new Date("2006-06-15T00:00:00+00:00"),
... DateEnd: "NULL",
... Current: "TRUE",
... Instrument_Type: "Continuous (Reference)"},
... {
... Date_Time : new Date("2020-01-01T05:00:00+00:00"),
... Nox : 16.8802,
... No2 : 15.7795,
... No : 0.7178,
... SiteID : 452,
... PM10 : 24.155,
... NVPM10 : "NULL",
... VPM10 : "NULL",
... NVPM2_5: "NULL",
... PM2_5: 21,
... VPM2_5: "NULL",
... CO: "NULL",
... O3: "NULL",
... SO2: "NULL",
... Temperature: 3,
... RH: "NULL",
... Air_Pressure: "NULL",
... Location: "AURN St Pauls",
... geo_point_2d: "51.4628294172,-2.58454081635",
... DateStart: new Date("2006-06-15T00:00:00+00:00"),
... DateEnd: "NULL",
... Current: "TRUE",
... Instrument_Type: "Continuous (Reference)"},
... {
... Date_Time : new Date("2020-01-02T00:00:00+00:00"),
... Nox : 14.5132,
... No2 : 14.0665,
... No : 0.2913,
... SiteID : 452,
... PM10 : 7.73,
... NVPM10 : "NULL",
... VPM10 : "NULL",
... NVPM2_5: "NULL",
... PM2_5: 10,
... VPM2_5: "NULL",
... CO: "NULL",
... O3: "NULL",
... SO2: "NULL",
... Temperature: 6.6,
... RH: "NULL",
... Air_Pressure: "NULL",
... Location: "AURN St Pauls",
... geo_point_2d: "51.4628294172,-2.58454081635",
... DateStart: new Date("2006-06-15T00:00:00+00:00"),
... DateEnd: "NULL",
... Current: "TRUE",
... Instrument_Type: "Continuous (Reference)"},
... {
... Date_Time : new Date("2020-01-02T10:00:00+00:00"),
... Nox : 24.8593,
... No2 : 19.2602,
... No : 3.6517,
... SiteID : 452,
... PM10 : 11.594,
... NVPM10 : "NULL",
... VPM10 : "NULL",
... NVPM2_5: "NULL",
... PM2_5: 7,
... VPM2_5: "NULL",
... CO: "NULL",
... O3: "NULL",
... SO2: "NULL",
... Temperature: 8.1,
... RH: "NULL",
... Air_Pressure: "NULL",
... Location: "AURN St Pauls",
... geo_point_2d: "51.4628294172,-2.58454081635",
... DateStart: new Date("2006-06-15T00:00:00+00:00"),
... DateEnd: "NULL",
... Current: "TRUE",
... Instrument_Type: "Continuous (Reference)"}])
```

**Output to confirm that "ObjectId" created for each document**

```
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("61db371ecbc0e94f516b6d5c"),
                ObjectId("61db371ecbc0e94f516b6d5d"),
                ObjectId("61db371ecbc0e94f516b6d5e"),
                ObjectId("61db371ecbc0e94f516b6d5f"),
                ObjectId("61db371ecbc0e94f516b6d60")
        ]
}

```

**To check the data in the Collection "bristol_air_quality_data"**

```
> db.bristol_air_quality_data.find().pretty()

```
**Output**
```
{
        "_id" : ObjectId("61db371ecbc0e94f516b6d5c"),
        "Date_Time" : ISODate("2020-11-05T19:00:00Z"),
        "Nox" : 264.881,
        "No2" : 65.025,
        "No" : 130.343,
        "SiteID" : 452,
        "PM10" : 86.958,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 62,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : 2.994,
        "SO2" : "NULL",
        "Temperature" : "NULL",
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
{
        "_id" : ObjectId("61db371ecbc0e94f516b6d5d"),
        "Date_Time" : ISODate("2020-01-01T00:00:00Z"),
        "Nox" : 29.037,
        "No2" : 27.1229,
        "No" : 1.2484,
        "SiteID" : 452,
        "PM10" : 44.445,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 40,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : "NULL",
        "SO2" : "NULL",
        "Temperature" : 3.3,
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
{
        "_id" : ObjectId("61db371ecbc0e94f516b6d5e"),
        "Date_Time" : ISODate("2020-01-01T05:00:00Z"),
        "Nox" : 16.8802,
        "No2" : 15.7795,
        "No" : 0.7178,
        "SiteID" : 452,
        "PM10" : 24.155,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 21,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : "NULL",
        "SO2" : "NULL",
        "Temperature" : 3,
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
{
        "_id" : ObjectId("61db371ecbc0e94f516b6d5f"),
        "Date_Time" : ISODate("2020-01-02T00:00:00Z"),
        "Nox" : 14.5132,
        "No2" : 14.0665,
        "No" : 0.2913,
        "SiteID" : 452,
        "PM10" : 7.73,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 10,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : "NULL",
        "SO2" : "NULL",
        "Temperature" : 6.6,
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
{
        "_id" : ObjectId("61db371ecbc0e94f516b6d60"),
        "Date_Time" : ISODate("2020-01-02T10:00:00Z"),
        "Nox" : 24.8593,
        "No2" : 19.2602,
        "No" : 3.6517,
        "SiteID" : 452,
        "PM10" : 11.594,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 7,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : "NULL",
        "SO2" : "NULL",
        "Temperature" : 8.1,
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
```
**To check summary of the database**
```
> db.stats()

```
**Output**

```
{
        "db" : "pollution_db",
        "collections" : 1,
        "views" : 0,
        "objects" : 5,
        "avgObjSize" : 463,
        "dataSize" : 2315,
        "storageSize" : 20480,
        "freeStorageSize" : 0,
        "indexes" : 1,
        "indexSize" : 20480,
        "indexFreeStorageSize" : 0,
        "totalSize" : 40960,
        "totalFreeStorageSize" : 0,
        "scaleFactor" : 1,
        "fsUsedSize" : 100008873984,
        "fsTotalSize" : 209662767104,
        "ok" : 1
}
```

**Query in MongoDB -  Return the Documents where Nox and No2 are greater than 20**

```
 > db.bristol_air_quality_data.find({$and: [{"Nox" : {$gt:20}}, {"No2" : {$gt:20}}]}).pretty()
 
 ```
**Output**
```
 {
        "_id" : ObjectId("61db371ecbc0e94f516b6d5c"),
        "Date_Time" : ISODate("2020-11-05T19:00:00Z"),
        "Nox" : 264.881,
        "No2" : 65.025,
        "No" : 130.343,
        "SiteID" : 452,
        "PM10" : 86.958,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 62,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : 2.994,
        "SO2" : "NULL",
        "Temperature" : "NULL",
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
{
        "_id" : ObjectId("61db371ecbc0e94f516b6d5d"),
        "Date_Time" : ISODate("2020-01-01T00:00:00Z"),
        "Nox" : 29.037,
        "No2" : 27.1229,
        "No" : 1.2484,
        "SiteID" : 452,
        "PM10" : 44.445,
        "NVPM10" : "NULL",
        "VPM10" : "NULL",
        "NVPM2_5" : "NULL",
        "PM2_5" : 40,
        "VPM2_5" : "NULL",
        "CO" : "NULL",
        "O3" : "NULL",
        "SO2" : "NULL",
        "Temperature" : 3.3,
        "RH" : "NULL",
        "Air_Pressure" : "NULL",
        "Location" : "AURN St Pauls",
        "geo_point_2d" : "51.4628294172,-2.58454081635",
        "DateStart" : ISODate("2006-06-15T00:00:00Z"),
        "DateEnd" : "NULL",
        "Current" : "TRUE",
        "Instrument_Type" : "Continuous (Reference)"
}
```

