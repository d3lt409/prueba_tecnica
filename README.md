# Prueba técnica
Desarrollo de la prueba técnica, en esta se desarrollan dos pruebas

# Instalación
Para que esta prueba funcione, se debe instalar las librerías que se encuentran en el archivo <strong>requirements.txt</strong>, se instala de la siguiente manera desde un command line ya sea Windows o Linux: 

    python -m pip install -r requirements.txt

# Contenido

Todo se encuentra dentro de la carpeta <strong>src</strong>, aquí se tienen dos carpetas que corresponden a cada prueba:

- ## prueba_1 
Aquí se tiene un archivo llamado <strong>prueba_tecnica_1.py</strong> este es archivo principal, al ejecutarse empezará a ejecutar lo que se solicita cada minuto, hasta que le den orden de parar

- ## prueba_2
Aquí se tienen tres archivos de <strong>python</strong>  y un archivo de <strong>sqlite</strong>
  - ### Archivos de python
    + <strong>models.py</strong> dentro de este se tiene el el modelo de usuarios implementado con <strong>sqlalchemy</strong>
    + <strong>db.py</strong> este archivo es el que se encarga de hacer la conexión a la base de datos
    + <strong>app.py</strong> este es el archivo principal donde se ejecuta la prueba 2
  - ### Archivos de sqlite
    + <strong>db_prueba.sqlite</strong> este archivo es encargado de almacenar los modelos 

para utilizar esta prueba primero debe leer el manual que se puede visualizar ejecutando es línea 

    python src/prueba_2/app.py --help

Esto le mostrará todas las funciones que tiene implementada

Para cada función se tendrá un manual, por ejemplo

    python src/prueba_2/app.py create-user --help

## Ejemplo de creación de usuario

    python src/prueba_2/app.py create-user -n Andres -l Herrera -a 22 -e andres_herrera@gmail.com

Aquí se está creando al usuario Andres Herrera con la edad de 22 años y con el correo andres_herrera@gmail.com

## Ejemplo para ver todos los usuarios

    python src/prueba_2/app.py get-users

Aquí muestra el listado de usuarios