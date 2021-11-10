# Proyecto Aplicación Cálculo de Índice de Masa Corporal.

Aplicación que permite calcular el Índice de Masa Corporal.  
Desarrollada para actividad taller curso Testing y Calidad de Software - Universidad Andrés Bello.  
Chile.  

## Como Iniciar Aplicación

Detalle de consideraciones a tener en cuenta para el despliegue de la aplicación

### `Versión de Python`

<<<<<<< HEAD
Para el desarrollo de esta app se tuliza python en su versión 3.9.1
=======
Para el desarrollo de esta app se utilizó python en su versión 3.9.1
>>>>>>> 4733da1 (Modificaciones archivo readme)

### `Desarrollo UI con Tkinter`

Para el desarrollo de interfaces de usuario se utilizo la biblioteca Tkinter.  
Tkinter es un binding de la biblioteca gráfica Tcl/Tk para el lenguaje de programación Python. Se considera un estándar para la interfaz gráfica de usuario (GUI) para Python y es el que viene por defecto con la instalación para Microsoft Windows.

### `Despliegue`

Para iniciar la app solo debe utilizar el comando "python main.py" desde una terminal. Para ejecutar el comando, se debe abrir la terminal en la raíz del directorio del proyecto, asumiendo que su versión de python incluye por defecto la biblioteca de Tkinter, en caso contrario deberá instalar dicha biblioteca.

## Detalle de Componentes

<<<<<<< HEAD
Se entrega a continuación una breve descripción de los componentes que integran la aplicación, y el contenido de cada uno de ellos.
### `Componente WindowsApp`

Este componente contiene las ventanas UI de la aplicación:  

- main.py: Ventana incial que muestra un menú con opciones para registrarse en caso de ser usuario nuevo, o iniciar sesión si ya eres usuario registrado.  
- registerDataWindow.py: Ventana formulario que permite ingresar un email y contraseña para registrar una cuenta de usuario antes de pasar a registrar los datos personales.
- personDataWindow.py: Ventana formulario que permite ingresar los datos personales para registrar un usuario en la aplicación.  
- loginWindow.py: Ventana formulario que permite a un usuario registrado poder inicar sesión para utilizar la aplicación.  
- appUserOptionsWindows.py: Ventana que contiene las opciones a las que puede acceder un usuario registrado (calcular IMC y Revisar Historial IMC).  
- imcDataWindow.py: Ventana formulario que permite al usuario ingresar los datos necesarios para el cálculo del IMC (fecha, hora, peso y estatura).  
- imcReportWindow.py: Ventana que muestra el historial de IMC registrados por un usuario.  

En el caso de los archivos registerDatawindow.py, personDataWindow.py, loginWindow.py e imcDataWindow.py, dentro de cada una de estos se define una función que maneja la funcionalidad de la ventana, y que se dispara desde el botón de acción de cada una de ellas. Su trabajo es la de tomar los valores de las entradas de formulario y enviarlos a los componentes que los gestionan para ser procesados.

### `Componente Helpers`

La carpeta Helpers contiene un archivo llamado "helpersFunctions.py". Este contiene 9 funciones que evaluan que un input dado se encuentré dentro de patrones pre-definidos para el correcto funcionamiento de la aplicación, y que su retorno es de tipo boolean. Además contiene 2 funciones que retornan la fecha y hora actual.

### `Componente Handler`

Este componente contiene 3 archivos:  

El primero llamado handlerImc.py define 4 funciones, una para calcular el imc, otras dos para evaluar el rango de imc en que se encuentra el valor dado, una para hombre y otra para mujer, y una cuarta función que integra las dos anteriores.  
  
El segundo archivo llamado handlerUserDataPersistence.py define 7 funciones para el manejo de datos persistente de la app. 3 de estas funciones graban datos en formato json en archivos planos, además ahora implementan control de excepciones y retornan un valor de tipo boolean para indicar el resultado del proceso. Las otras 4 funciones retornan data, y se utilizan para recuperar datos desde el repositorio de archivos planos.  
  
El tercer archivo llamado handlerWindowValidation.py define 3 funciones que se utilizan para validar las entradas de datos desde ventanas de formulario, como ingreso de credenciales (ventanas de registro y login), ingreso de datos de persona y el ingreso de datos de IMC. Estas funciones definen retorno en formato de tipo diccionario python, que proporcionan una propiedad llamada ‘response’ de tipo boolean y otra propiedad llamada ‘message’. Estas se utilizan con el objetivo de entregar información sobre el resultado de las validaciones de entradas, por ejemplo, si en el formulario de datos personales el usuario ingresa un género no válido, la validación retornaría ‘response’ en false y en ‘message’ indicaría que el género es el problema.  

=======
Se entrega a continuación una breve descripción de los componentes que integran la aplicación, y el contenido de cada uno de ellos.  

- main.py: Este archivo se encuentra en la raíz del proyecto, y es la ventana incial que muestra un menú con opciones para registrarse en caso de ser usuario nuevo, o iniciar sesión si ya eres usuario registrado.  

### `Componente WindowsApp`

Este componente contiene las ventanas UI de la aplicación:  

- registerDataWindow.py: Ventana formulario que permite ingresar un email y contraseña para registrar una cuenta de usuario antes de pasar a registrar los datos personales.
- personDataWindow.py: Ventana formulario que permite ingresar los datos personales para registrar un usuario en la aplicación.  
- loginWindow.py: Ventana formulario que permite a un usuario registrado poder inicar sesión para utilizar la aplicación.  
- appUserOptionsWindow.py: Ventana que contiene las opciones a las que puede acceder un usuario registrado (calcular IMC y Revisar Historial IMC).  
- imcDataWindow.py: Ventana formulario que permite al usuario ingresar los datos necesarios para el cálculo del IMC (fecha, hora, peso y estatura).  
- imcReportWindow.py: Ventana que muestra el historial de IMC registrados por un usuario.  

En el caso de los archivos registerDatawindow.py, personDataWindow.py, loginWindow.py e imcDataWindow.py, dentro de cada una de ellos se define una función que maneja la funcionalidad de la ventana, y que se dispara desde el botón de acción de cada una de ellas. Su trabajo es la de tomar los valores de las entradas de formulario y enviarlos al componente que los procesa.

### `Componente Helpers`

La carpeta Helpers contiene un archivo llamado "helpersFunctions.py". Este contiene 9 funciones que evaluan que un input dado se encuentré dentro de patrones pre-definidos para el correcto funcionamiento de la aplicación, y su retorno es de tipo boolean. Además contiene 2 funciones que retornan la fecha y hora actual.

### `Componente Handler`

Este componente contiene 3 archivos:  

El primero llamado handlerImc.py define 4 funciones, una para calcular el imc, otras dos para evaluar el rango de imc en que se encuentra el valor dado, una para hombre y otra para mujer, y una cuarta función que integra las dos anteriores.  
  
El segundo archivo llamado handlerUserDataPersistence.py define 7 funciones para el manejo de datos persistente de la app. 3 de estas funciones graban datos en formato json en archivos planos, además ahora implementan control de excepciones y retornan un valor de tipo boolean para indicar el resultado del proceso. Las otras 4 funciones retornan data, y se utilizan para recuperar datos desde el repositorio de archivos planos.  
  
El tercer archivo llamado handlerWindowValidation.py define 3 funciones que se utilizan para validar las entradas de datos desde ventanas de formulario, como ingreso de credenciales (ventanas de registro y login), ingreso de datos de persona y el ingreso de datos de IMC. Estas funciones definen retorno en formato de tipo diccionario python, que proporcionan una propiedad llamada ‘response’ de tipo boolean y otra propiedad llamada ‘message’. Estas se utilizan con el objetivo de entregar información sobre el resultado de las validaciones de entradas, por ejemplo, si en el formulario de datos personales el usuario ingresa un género no válido, la validación retornaría ‘response’ en false y en ‘message’ indicaría que el género es el problema.  

>>>>>>> 4733da1 (Modificaciones archivo readme)
### `Componente Behaviors`  

Componente que contiene un archivo llamado windowBehavior.py, el cual define 4 funciones para manejar comportamientos como ventanas de alerta, de éxito y cierre.

### `Carpeta Data`  

<<<<<<< HEAD
<<<<<<< HEAD
Esta carpeta es requerida por la aplicación para persistir datos en archivos planos.
=======
Esta carpeta es requerida por la aplicación para persistir datos en archivos planos.
>>>>>>> 4733da1 (Modificaciones archivo readme)
=======
Esta carpeta es requerida por la aplicación para persistir datos en archivos planos.
>>>>>>> 35ee064 (Update README.md)
