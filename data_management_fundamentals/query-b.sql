#Return the mean values of PM2.5 (particulate matter <2.5 micron diameter) & VPM2.5 (volatile particulate matter <2.5 micron diameter) 
#by each station for the year 2019 for readings taken on or near 08:00 hours (peak traffic intensity).
SELECT station_readings.date_time AS "Reading Date", round(AVG(station_readings.pm2_5),2) AS "Mean of PM2.5",
round(AVG(station_readings.vpm2_5),2) AS "Mean of VPM2.5", station_readings.site_id AS "SiteID"  FROM station_readings
WHERE YEAR (station_readings.date_time) = 2019 and DATE_FORMAT(station_readings.date_time,'%H:%i:%s') = '08:00:00'
GROUP BY (station_readings.site_id);


 
