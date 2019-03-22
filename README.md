# TC3041-P2-Primavera-2019

Orientaciones para la **Práctica 2. Bases de datos orientadas a documentos**

Consulte el documento PDF que aparece en el repositorio

Instrucciones de uso:

Para compilar el archivo Clientes.cpp, se requiere C++11

Para utilizar el programa MongoQueries.py se requiere de la librería de MongoDB de Python: https://docs.mongodb.com/ecosystem/drivers/python/

MongoQueries.py se conecta a la base de datos por el puerto 27018 y realiza las siguientes consultas:

Obtiene a todos los clientes que se apelliden Junson y los ordena en orden alfabético inverso. Cambia el nombre de Nombre_Completo por Nombre Competo y Cuenta por Número de Cuenta. No muestra el _id.

    db.clientes.aggregate([{"$match":{"Nombre_Completo":{"$regex":".*Junson"}}},{"$sort":{"Nombre_Completo":-1}},{"$project":{"_id":0,"Nombre Completo":"$Nombre_Completo","Número de Cuenta":"$Cuenta"}}]);


Obtiene las 25 cuentas con los saldos más altos y las ordena de mayor a menor. Cambia el nombre de Cuenta por Número de Cuenta. No muestra el _id.

    db.cuentas.aggregate([{"$sort":{"Saldo":-1}},{"$limit":25},{"$project":{"_id":0,"Número de Cuenta":"$Cuenta","Saldo":1}}]);

Obtiene las 25 cuentas origen que han realizado la mayor cantidad de transferencias y las ordena de mayor a menor, también muestra el valor promedio de las transferencias. Cambia el nombre de Cuenta_Origen por Cuenta Origen.

    db.transferencias.aggregate([{"$group":{"_id":{"Cuenta Origen":"$Cuenta_Origen"}, "total":{"$sum":1},"promedio":{"$avg":"$Monto"}}},{"$project":{"_id":1,"Transacciones realizadas":"$total","Promedio":"$promedio"}},{"$sort":{"Transacciones realizadas":-1}},{"$limit":25}]);

El archivo Clientes.cpp genera 3 archivos:

* clientes.json que contiene 100500 Cuentas diferentes cada una con un nombre de cliente.
* cuentas.json que contiene 100500 Cuentas diferentes cada una con un saldo.
* transferencias.json que contiene 100500 Cuentas diferentes cada una con una cuenta orígen, cuenta destino, monto transferido y fecha.

Para importar estos archivos a MongoDB, se recomienda usar: 

    mongoimport -d Banco -c clientes --jsonArray clientes.json
    mongoimport -d Banco -c cuentas --jsonArray cuentas.json
    mongoimport -d Banco -c transferencias --jsonArray transferencias.json
