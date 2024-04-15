-- create_states.sql
-- author: jared arroyo ruiz

-- appropiate data types for each column in
-- the us-state-pop.csv dateset

DROP TABLE IF EXISTS states_list;
CREATE TABLE states_list (
code TEXT,
state TEXT,
population NUMERIC(8,0)
);