/* commands in cap. Use smeicolons */

/* to create a new data table */
CREATE TABLE simulationdata (simname TEXT, simnum INTEGER, simlength INTEGER);

/* use constraints in the data table */
CREATE TABLE simulationdata (
  simname TEXT PRIMARY KEY, /* i.e. must be unique. Used once per table. UNIQUE is similar, can be used more than once */ 
  simnum INTEGER NOT NULL,  /* must not be empty */
  simlength INTEGER DEFAULT 100); /* set a default value */

/* adding info */
INSERT INTO simulationdata (simname, simnum, simlength) VALUES ('WT_ADP', 1, 1000);

/* editing data */
UPDATE simulationdata
SET simlength = 1050
WHERE simname = 'WT_ADP'

/* add column */
ALTER TABLE simulationdata ADD COLUMN forcefield TEXT; 

/* delete rows with NULL in specified column */
DELETE FROM simulationdata WHERE forcefield IS NULL; 

/* querying data */
SELECT * FROM simulationdata;
SELECT simname FROM simulationdata;
SELECT simname, simlength FROM simulationdata;
SELECT * FROM simnames WHERE simlength BETWEEN 100 AND 200;
SELECT * FROM WHERE simlength > 500;
SELECT * FROM simnames WHERE name BETWEEN 'A' AND 'J';
SELECT * FROM simnames WHERE simname LIKE 'ADP%'; /* % is a wildcard for zero or more letters */
SELECT * FROM simnames WHERE simname LIKE '%_WT'; 
SELECT * FROM simnames WHERE simlength BETWEEN 100 AND 200 and forcefield = 'OPLS' or simname = "WT_*';
SELECT * FROM simnames ORDER BY simlength DESC LIMIT 3; /* DESC = descending order LIMIT = head/tail */

SELECT DISTNCT simlength FROM simulationdata;

