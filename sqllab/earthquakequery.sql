-- earthquakequery.sql
-- author: jared arroyo ruiz

-- the following file will contain three 
-- queries to answer questions about the
-- earthquake dataset


-- Find all earthquakes that have a magnitude
-- less than 2.5
-- According to Michigan Tech, earthquakes of this
-- magnitude are usually not felt
SELECT * FROM earthquakes WHERE magnitude < 2.5;

-- Identify the greatest value of magnitude error
SELECT MAX(magerror) FROM earthquakes;

-- Identify all earthquakes where the 'dmin' value
-- is less than .01.
-- According to the ANSS, 'dmin' reveals the distance
-- from the epicenter of the earthquake to the nearest
-- station. So, the smaller a dmin value, the more reliable
-- the calculated depth of the earthquake is.
SELECT * FROM earthquakes WHERE dmin < .01;
