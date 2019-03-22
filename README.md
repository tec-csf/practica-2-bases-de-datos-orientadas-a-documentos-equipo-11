# TC3041-P2-Primavera-2019

Orientaciones para la **Práctica 2. Bases de datos orientadas a documentos**

Consulte el documento PDF que aparece en el repositorio


Para compilar el archivo Clientes.cpp, se requiere C++11

Para utilizar el programa MongoQueries.py se requiere de la librería de MongoDB de Python: https://docs.mongodb.com/ecosystem/drivers/python/

El archivo Clientes.cpp genera 3 archivos:

* clientes.json que contiene 100500 Cuentas diferentes cada una con un nombre de cliente.
* cuentas.json que contiene 100500 Cuentas diferentes cada una con un monto.
* transferencias.json que contiene 100500 Cuentas diferentes cada una con un nombre de cliente.

Para importar estos archivos a MongoDB, se recomienda usar: 

mongoimport -d Banco -c clientes --jsonArray clientes.json

mongoimport -d Banco -c cuentas --jsonArray cuentas.json

mongoimport -d Banco -c transferencias --jsonArray transferencias.json
