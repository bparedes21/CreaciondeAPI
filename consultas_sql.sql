DROP TABLE IF EXISTS races;
CREATE TABLE races (
    raceId INTEGER NOT NULL,
    year INTEGER,
	round INTEGER,
    circuitId INTEGER  NOT NULL,
    name TEXT,
    date TEXT,
    time TEXT,
    url TEXT,	
)

SELECT * FROM races

DROP TABLE IF EXISTS results
CREATE TABLE results (
    resultId INTEGER NOT NULL,
    raceId INTEGER NOT NULL,
	driverId INTEGER NOT NULL,
    constructorId INTEGER NOT NULL,
    number INTEGER,
    grid REAL,
    position INTEGER,
    positionText REAL,
    positionOrder	INTEGER,
    points	REAL,
    laps INTEGER,
	time TEXT,
    milliseconds TEXT,
	fastestLap INTEGER,
	rank INTEGER,
    fastestLapTime TEXT,
    fastestLapSpeed REAL,
    statusId INTEGER
	
)
SELECT * FROM results

DROP TABLE IF EXISTS drivers
CREATE TABLE drivers (
    driverId INTEGER NOT NULL,
    driverRef TEXT,
	number REAL,
    code TEXT,
    dob TEXT,
    nationality TEXT,
    url TEXT,
    forename TEXT,	
    surname TEXT,	
)
SELECT * FROM drivers
DROP TABLE IF EXISTS circuits


CREATE TABLE circuits (
    circuitId INTEGER NOT NULL,
    circuitRef TEXT,
	name REAL,
    location TEXT,
    country TEXT,
    lat TEXT,
    lng TEXT,
    alt INTEGER,	
    url TEXT,	
)

SELECT * FROM circuits

DROP TABLE IF EXISTS constructors
CREATE TABLE constructors (
    constructorId INTEGER NOT NULL,
    constructorRef TEXT,
	name REAL,
    location TEXT,
    country TEXT,
    lat TEXT,
    lng TEXT,
    alt INTEGER,	
    url TEXT,	
)
SELECT * FROM constructors

/* 

El año con más carreras
El nombre del corredor con mayor cantidad de primeros puestos
El nombre del circuito con mas recorrido
El nombre del corredor con mayor cantidad de puntos en total*/

SELECT r."year", COUNT(r.raceId) as cantidad_de_carreras FROM races as r
GROUP BY r."year"
ORDER BY   cantidad_de_carreras DESC   ,r."year"  ASC
LIMIT 1


SELECT d.forename, d.surname,results.cant_de_primeros_puestos  FROM drivers d 
INNER JOIN
(
SELECT res.driverId  , res."rank"  , COUNT(res."rank") as cant_de_primeros_puestos  FROM results  as res
WHERE res."rank"  ="1"
GROUP BY res.driverId
ORDER BY   cant_de_primeros_puestos DESC   
LIMIT 1
) as results 
ON results.driverId  = d.driverId 

SELECT  races.name as nombre_de_la_carrera , circuits.name as nombre_de_circuito , SUM( r.laps)  as cantidad_de_recorrido_vueltas FROM results r 
INNER JOIN 
races on races.raceId = r.raceId
INNER JOIN 
circuits ON circuits.circuitId  = races.circuitId 
GROUP BY nombre_de_circuito
ORDER BY  cantidad_de_recorrido_vueltas  DESC 


SELECT  d.forename ,d.surname , SUM(points) AS cantidad_de_puntos_en_total FROM results r 
INNER JOIN
drivers d on d.driverId = r.driverId 
