#Extend the previous query to show these values for all stations in the years 2010 to 2019.
SELECT station_readings.date_time AS "Reading Date", round(AVG(station_readings.pm2_5),2) AS "Mean of PM2.5",
round(AVG(station_readings.vpm2_5),2) AS "Mean of VPM2.5", station_readings.site_id AS "SiteID"  FROM station_readings
WHERE YEAR (station_readings.date_time) BETWEEN 2010 AND  2019 AND DATE_FORMAT(station_readings.date_time,'%H:%i:%s') = '08:00:00'
GROUP BY (station_readings.site_id);