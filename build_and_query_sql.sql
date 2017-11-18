/* commands in cap. Use smeicolons */
/* based on codeacademy as a resource */

/* to create a new data table */
CREATE TABLE simulationdata (simname TEXT, simnum INTEGER, simlength INTEGER);

/* use constraints in the data table */
CREATE TABLE simulationdata (
  simname TEXT PRIMARY KEY, /* i.e. must be unique. Used once per table. UNIQUE is similar, can be used more than once */ 
  simnum INTEGER NOT NULL,  /* must not be empty */
  simlength INTEGER DEFAULT 100, /* set a default value */
  FOREIGN KEY(forcefield) REFERENCE difftable(columm) /* FOREIGN KEY restrains input, in this case to a column from a different table */
; 
  
DROP TABLE IF EXISTS simulationdata /*  drop a table or do nothing, depending on if the table already exists */
CREATE TABLE IF NOT EXISTS simulationdata (
  simname TEXT PRIMARY KEY, 
  simnum INTEGER NOT NULL,  
  simlength INTEGER DEFAULT 100);

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
SELECT * FROM simulationdata WHERE simlength BETWEEN 100 AND 200;
SELECT * FROM WHERE simlength > 500;
SELECT * FROM simulationdata WHERE name BETWEEN 'A' AND 'J';
SELECT * FROM simulationdata WHERE simname LIKE 'ADP%'; /* % is a wildcard for zero or more letters */
SELECT * FROM simulationdata WHERE simname LIKE '%_WT'; 
SELECT * FROM simulationdata WHERE simlength BETWEEN 100 AND 200 and forcefield = 'OPLS' or simname = "WT_*";
SELECT * FROM simulationdata ORDER BY simlength DESC LIMIT 3; /* DESC = descending order LIMIT = head/tail */
SELECT DISTNCT simlength FROM simulationdata;

/* aggregate functions: perform calc on set of values at return one value */
/* only ~80 % certain on the syntax */

SELECT COUNT(*) FROM simulationdata; /* count number of rows */
SELECT simlength, COUNT(*) FROM simulationdata GROUP BY simlength;
SELECT simlength, COUNT(*) FROM simulationdata WHERE simnum > 2 GROUP BY simlength;
SELECT SUM(simlength) FROM simulationdata;
SELECT MAX(simlength) FROM simulationdata;
SELECT simname, forcefield, MAX(simlength) FROM simulationdata GROUP BY forcefield;
SELECT simname, forcefield, MIN(simlength) FROM simulationdata GROUP BY forcefield;
SELECT AVG(simlength) FROM simulationdata;
SELECT forcefield, AVG(simlength) FROM simulationdata GROUP BY forcefield;
SELECT forcefield, ROUND(AVG(simlength), 2) FROM simulationdata GROUP BY forcefield;

/* Multiple tables */
CREATE TABLE analyses(id INTEGER PRIMARY KEY, rmsd INTEGER, name TEXT);
SELECT * FROM simulationdata WHERE analyses_rmsd > 4; /* A foreign key is a column that contains the primary key of another table in the database */
SELECT simulationdata.simname, simnames.forcefield, analyses.rmsd FROM simulationdata, analyses; /* cross join- table_name.column_name */
SELECT * FROM simulationdata JOIN analyses ON simulationdata.analyses_rmsd = simulationdata.rmsd; /*  inner join will combine rows from different tables if the join condition is true */
SELECT * FROM simulationdata JOIN LEFT ses ON simulationdata.analyses_rmsd = simulationdata.rmsd; /* outer join (LEFT). Do not require join condition to be met */
AS /* alias - rename a column to prevent duplication */
SELECT simulationdata.simname AS 'Name of simulation' FROM simnames

