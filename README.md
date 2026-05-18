# predictor-nacionalidad-api

## Integrantes

- Maia Uranga
- Catalina Salse
- Belen Blaksley

## Descripción del proyecto

El objetivo es desarrollar un programa en Python que consulte una API externa para estimar posibles nacionalidades asociadas a un nombre ingresado por el usuario.

El programa utiliza la API de Nationalize.io. El usuario ingresa un nombre y el sistema devuelve una lista de países probables, junto con la probabilidad asociada a cada país.

## Funcionalidades principales

El programa cuenta con un menú principal con tres opciones:

1. Consultar un nombre.
2. Comparar dos nombres.
3. Salir del programa.

### Opción 1: Consultar un nombre

El usuario ingresa un nombre y el programa muestra:

- Nombre consultado.
- Cantidad de registros utilizados por la API.
- Lista de países probables.
- Probabilidad asociada a cada país.
- País con mayor probabilidad.

### Opción 2: Comparar dos nombres

El usuario ingresa dos nombres.  
El programa consulta la API para cada uno y muestra un resumen con el país más probable y su probabilidad correspondiente.

### Opción 3: Salir

Finaliza la ejecución del programa mostrando un mensaje de cierre.

## Estructura del repositorio
predictor-nacionalidad-api/
- main.py
- api_nacionalidad.py
- README.md
