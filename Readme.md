<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

<div align = "center">
<img src="/img/races.jpg" width="400 px">

# [Proyecto :checkered_flag:  RaceResults :triangular_flag_on_post: ETL, creacion de DB en SQLITE](#)


<H2>¡ :crossed_flags:  Apreta aca :point_down: para ir a ver la API con las respuestas! :vertical_traffic_light:! </H2>

:sunrise_over_mountains: [Races, drivers, circuits, results](https://api-races.vercel.app/docs) - Deploy de API 

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
│ 
│── extraer_datos.py
│── transformar_datos.py
│── crear_db.py
│── carga_de_datos_db.py
│── Racing_db.db
│── consultas_sql
│ 
└── README.md
```

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>
  
******************************************************************************

# Carrera a la Eficiencia: ETL y API para Datos de Carreras, Pilotos y Circuitos

En el emocionante mundo de las carreras, donde cada milisegundo cuenta, la gestión de datos es tan crucial como la velocidad en la pista. Este proyecto es mucho más que un simple proceso ETL (Extracción, Transformación y Carga) de datos relacionados con carreras, pilotos, circuitos y resultados. Va más allá al crear una robusta base de datos SQLite, transformando datos crudos en un recurso estratégico.

## About 
### Descripción del Proyecto

Este proyecto se sumerge en el universo de las competiciones automovilísticas, extrayendo datos esenciales para proporcionar insights significativos. A través de un proceso ETL eficiente, los datos se transforman y cargan en una base de datos SQLite, convirtiéndolos en una fuente accesible y potente.

# Objetivo Principal

La finalidad principal de este proyecto es facilitar el acceso a la rica información generada por las carreras. Lo logra mediante una API intuitiva con endpoints específicos para consultas, brindando a los usuarios la capacidad de acelerar el acceso y análisis de datos en este emocionante universo.

## Características Destacadas

- **Proceso ETL Robusto:** Desde la extracción hasta la carga, cada paso está diseñado para optimizar la eficiencia y la calidad de los datos.
  
- **Base de Datos SQLite:** Se crea una base de datos sólida que almacena la información procesada, asegurando la disponibilidad y la integridad de los datos.

- **API Potente:** La interfaz API ofrece endpoints específicos para consultas, proporcionando una experiencia ágil y personalizada para los usuarios.

Este proyecto es el aliado perfecto para aquellos que buscan no solo datos, sino información valiosa que impulsa decisiones estratégicas en el mundo de las carreras. Prepárate para vivir una experiencia de datos que acelera hacia la victoria. 🏎️🚀
## Proceso ETL

### Extracción de Datos:
- Los datos se extraen desde diversas fuentes.

### Transformación de Datos:
- Eliminación de columnas con más del 30% de datos faltantes.
- Verificación de registros duplicados.
- Limpieza de caracteres, incluyendo la eliminación de acentos, conversión a minúsculas y manejo de campos con "\N".

### Carga de Datos en la Base de Datos SQLite:
- Se crea una base de datos llamada "Racing_db.db".
- Se generan tablas para almacenar información relevante.
  
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>

## Uso del Proyecto :factory: 



```markdown``` 

## Guía de uso del repositorio Este repositorio utiliza GitHub Actions con configuración YAML para flujos de trabajo automatizados. Siga estos pasos para utilizar el repositorio de manera eficaz: 


## Primeros pasos 

1. **Clonar el repositorio:** 

```bash git clone <repository-url>``` 

2. **Navegar al repositorio:** 

``` bash cd <directorio-repositorio>``` 

3. **Explore los flujos de trabajo YAML:** 

- Abra el directorio `.github/workflows` para buscar archivos de flujo de trabajo YAML. 
 
## Uso del flujo de trabajo proporcionado 
 
1. **Seleccione Flujo de trabajo:**

2. **-El archivo a utilizar se llama `python-package-conda.yml`.**

3. **Credenciales de Azure:**
   - Puede interactuar con Azure

4. **Ver la Ejecución del Flujo de Trabajo:**
   - Visite la pestaña "Actions" en GitHub para monitorear el progreso y los resultados del flujo de trabajo.


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
