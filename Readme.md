<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

<div align = "center">
<img src="/img/races.jpg" width="400 px">

# [:checkered_flag: RaceResults :triangular_flag_on_post: ](#)
  
</div>

<div align = "center">

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="20%"></a>

<H2> :crossed_flags: Apreta aca para ir a ver la API con las respuestas! :vertical_traffic_light: </H2>

:sunrise_over_mountains: [Races, drivers, circuits, results](https://creacionde-api.vercel.app/docs) - Deploy de API 

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

******************************************************************************
</div>

## Table of Contents

</br>
<div align = "center">

| | Table Of Contents |
|--|----------------|
| 1 | [About](#About)  |
| 2 | [Setup](#setup)  | 
| 3 | [Consultas_SQL](#Consultas_SQL)  | 

</div>
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

## Directory Structure

```js
├── .py-jupyter
│   │──
│   │──
│
│── funciones_py
│── Crear_db_SQLite_py.py
│── Racing_db.db
│── consultas_sql
│ 
└── README.md
```

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>
  
******************************************************************************

## About 

- `En este proyecto proceso los datos para garantizar su calidad y luego creo una API para ejecutar determinadas consultas facilitando la informacion obtenida.`

- `Completar de datos faltantes con web scraping. Luego las columnas con mas de 30% de datos faltantes fueron eliminadas.`

- `Comprobacion de que no hayan registros duplicados.`

- `Limpieza de caracteres: quitar acentos a las palabras ya que tenian acentos que no correspondian, pasar letras a minusculas, quitar espacios vacios delante o detras, campos con "\N" reemplazados con NaN segun su formato string , int, float.`

******************************************************************************

## Setup 

-Configuracion. Lista de librerias utilizadas

```js      

!pip install pandas
!pip install sqlite3

```

## Consultas_SQL


Se requiere saber:

- `El año con más carreras`

```
SELECT r."year", COUNT(r.raceId) as cantidad_de_carreras FROM races as r
GROUP BY r."year"
ORDER BY   cantidad_de_carreras DESC   ,r."year"  ASC
LIMIT 1
```

Resultado de la consulta:

<div align = "center">

| year | cantidad_de_carreras |
|--|----------------|
| 2021 | 23  |

</div>

- `El nombre del corredor con mayor cantidad de primeros puestos`

```

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

```

Resultado de la consulta:

<div align = "center">

| forename |  surname | cantidad_de_primeros_puestos |
|------|-----|-------------|
| lewis | hamilton  |   53       |

</div>


- `El nombre del circuito con mas recorrido`

```
SELECT  races.name as nombre_de_la_carrera , circuits.name as nombre_de_circuito , SUM( r.laps)  as cantidad_de_recorrido_vueltas FROM results r 
INNER JOIN 
races on races.raceId = r.raceId
INNER JOIN 
circuits ON circuits.circuitId  = races.circuitId 
GROUP BY nombre_de_circuito
ORDER BY  cantidad_de_recorrido_vueltas  DESC 
```

Resultado de la consulta:

<div align = "center">

| nombre_de_la_carrera |  nombre_de_circuito | cantidad_de_recorrido_vueltas |
|------|-----|-------------|
| monaco grand prix | Circuit de Monaco  |   75747      |

</div>


- `El nombre del corredor con mayor cantidad de puntos en total`

```
SELECT  d.forename ,d.surname , SUM(points) AS cantidad_de_puntos_en_total FROM results r 
INNER JOIN
drivers d on d.driverId = r.driverId 
```

Resultado de la consulta:

<div align = "center">

| forename |  surname | cantidad_de_puntos_en_total |
|------|-----|-------------|
| lewis | hamilton  |   44071.55      |

</div>

******************************************************************************
