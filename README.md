# pruebaCD

Luis Enrique Sánchez Lara

## Es necesario tener instalado Flask-SQLAlchemy, Pandas y MySQL.

Se debe ejecutar el archivo .sql y después ejecutar `flask run`.

## API

Para poblar se debe enviar una petición POST a `\seed` con el número de de registros en JSON.

Para llamar a la API se deben realizar peticiones POST y en el cuerpo se deben enviar las variables necesarias documentadas en cada función en formato JSON. 

`/colonias` busca las colonias por CP.
`/busqueda` busca por nombre
`/agrega` agrega nuevos datos.