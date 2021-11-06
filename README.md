# Proyecto Aplicación Cálculo de Índice de Masa Corporal.

Proyecto React JS. Desarrollado para la entrega del sprint N°2 curso Desarrollo Web Front End - Acamica.

## Decripción del Desarrollo del Proyecto

Para el desarrollo se consideraron los detalles siguientes:

### `Hook useState`

Se utilizó el hook useState para el manejo de estado de los filtros de la app. Bajo el concepto del "prop drilling" que se refiere al proceso de obtener datos en partes del árbol de componentes react, y así, llevar el estado y el manejador del useState a los lugares correctos de nuestra app.

### `Componentes`

Se crea dentro de carpeta "src" una subcarpeta llamada "components" para alojar los distintos componentes de la app.

-FiltrosNav: Componente que renderiza una barra nav con las distintas opciones de filtrado.
-Header: Componente que renderiza el header de la página, y que además muestra al usuario, en lenguaje natural, las opciones de filtrado seleccionadas. 
-Hotel: Componente "card" para mostrar la información correspndiente a un Hotel.
-Resultados: Componente que renderiza los resultados de hoteles según las opciones seleccionadas.
-Main: Componente que instancia los componentes anteriormente descritos para construir la app completa. Este componente es el que finalmente se instancia en app.js

### `Data`

Se crea dentro de carpeta "src" una subcarpeta llamada "data", la que contiene un archivo llamado data.js, y este ultimo es donde reside la data de todos los hoteles.
simula data que usualmente la obtendría desde un endpoint.

### `Enumeraciones`

Se crea dentro de carpeta "src" una subcarpeta llamada "enums", que contiene archivos javascript con datos constantes que utilizo dentro de la app.

### `Helpers`

Se crea dentro de carpeta "src" una subcarpeta llamada "helpers", que contiene archivos javascript con funciones que utilizo para manejar datos en componentes.

### `Imgs`

Se crea dentro de carpeta "src" una subcarpeta llamada "imgs", que contiene subcarpetas para alojar archivos svg, png y las imágenes para las card de hoteles.

## CodeSanbox del Proyecto

Puedes revisar el código de esta app y modificarlo online [haciendo click aquí](https://codesandbox.io/s/proyecto-hotel-react-4th5k).

### Enlace del Proyecto

Puedes utilizar la app en el siguiente enlace: [https://4th5k.csb.app/](https://4th5k.csb.app/).