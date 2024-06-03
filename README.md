# Dataset---Grupo-8

Para poder ejecutar el código fuente que nos facilita el dataset primero se debe instalar las bibliotecas Pandas y openpyxl  (necesaria para escribir archivos Excel). Se debe realizar lo siguiente:

* Abrir la consola de comandos (CMD)
* Ejecutar los siguientes comandos para instalar las bibliotecas:
  - pip install pandas
  - pip install openpyxl
La descarga y la instalación se hacen de manera automática.

Este código realiza lo siguiente:

* Carga los datos de un archivo CSV que contiene las respuestas de una encuesta sobre la Industria 4.0.
* Imprime información básica sobre el DataFrame para verificar su contenido.
* Rellena los valores nulos con cadenas vacías para evitar problemas
* Guarda el DataFrame procesado en un archivo Excel, excluyendo los índices del DataFrame, de estas forma:

