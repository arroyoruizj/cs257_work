DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time TIMESTAMPTZ,
  latitude FLOAT(5, 2),
  longitude FLOAT(5, 2),
  depth FLOAT(5, 2),
  magnitude FLOAT(3, 2),
  dmin FLOAT(5, 2),
  place STRING,
  horizontalError FLOAT(5, 2),
  depthError FLOAT(5, 2),
  magError FLOAT(3, 2),
  magNst INT(4)
);