DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time TIMESTAMPTZ,
  latitude NUMERIC(5, 2),
  longitude NUMERIC(5, 2),
  depth NUMERIC(5, 2),
  magnitude NUMERIC(3, 2),
  dmin NUMERIC(5, 2),
  place TEXT,
  horizontalError NUMERIC(5, 2),
  depthError NUMERIC(5, 2),
  magError NUMERIC(3, 2),
  magNst NUMERIC(4)
);