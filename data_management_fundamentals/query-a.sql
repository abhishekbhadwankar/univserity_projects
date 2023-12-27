#Return the date/time, station name and the highest recorded value of nitrogen oxide (NOx) found in the dataset for the year 2019.
SELECT date_format(station_readings.date_time, '%d-%M-%Y') AS "Reading Date", date_format(station_readings.date_time, '%H:%i:%s') AS "Reading Time", 
max(station_readings.nox) AS "Highest Recorded Nitrogen Oxide (NOx)", station_readings.site_id AS "SiteID", 
stations.location AS "Station Name" FROM station_readings
INNER JOIN stations ON station_readings.site_id = stations.site_id
WHERE YEAR (station_readings.date_time) = 2019;


