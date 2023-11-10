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

├── funciones_py
│── Crear_db_SQLite_py.py
│── Racing_db.db
│── consultas_sql
│ 
└── README.md
```

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"></a>
  
******************************************************************************

## About 
:car:

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
- `El nombre del corredor con mayor cantidad de primeros puestos`
- `El nombre del circuito con mas recorrido`
- `El nombre del corredor con mayor cantidad de puntos en total`




<details open> 
  
  <summary><h2>Deploy en Vercel</h2></summary>

  <p align="left"> 
     <h3>Ver su funcionamiento (haciendo click en logo Vercel 😃)</h3>
     <a href="https://creacionde-api.vercel.app/docs"><img width="200" src="img/vercel.svg" alt="creacion-de-api"></a>
   </p>
</details>
</div>
<div>
  
******************************************************************************

  <details open> 
   <summary><h2>Flujo de trabajo</h2></summary>
    <p align="left"> 
      <h3>Proceso</h3>
       <a href=""><img width="500" src="img/fluj de trabajo.svg" alt="flujo de trabajo"></a>
     </p>
  </details> 
</div>

<div>

******************************************************************************

  <details close> 
  <summary><h2>Videos en youtube</h2></summary>

<p align="left"> 
  <h3>Deploy sin heroku ejecutado localmente</h3>
  <a href="https://youtu.be/IXAubmGBM7g"><img width="278" src="https://img.youtube.com/vi/IXAubmGBM7g/0.jpg" alt=""></a>
  <h3>Deploy con heroku</h3>
  <a href="https://youtu.be/kQT8ulLdqfU"><img width="278" src="https://img.youtube.com/vi/kQT8ulLdqfU/0.jpg" alt=""></a>
 </p>
</div>
