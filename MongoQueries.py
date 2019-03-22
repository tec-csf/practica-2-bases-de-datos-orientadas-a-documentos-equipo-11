import pymongo
import pprint
from bson.son import SON

from pymongo import MongoClient

client = MongoClient('localhost', 27018)
db = client.Banco

collection = db.clientes

pipeline = [{"$match":{"Nombre_Completo":{"$regex":".*Junson"}}},
	{"$sort":{"Nombre_Completo":-1}},
	{"$project":{"_id":0,"Nombre Completo":"$Nombre_Completo","Número de Cuenta":"$Cuenta"}}]

pprint.pprint(list(collection.aggregate(pipeline)))

collection = db.cuentas

pipeline = [{"$sort":{"Saldo":-1}},
	{"$limit":25},
	{"$project":{"_id":0,"Número de Cuenta":"$Cuenta","Saldo":1}}]

pprint.pprint(list(collection.aggregate(pipeline)))

collection = db.transferencias

pipeline = [
	{
	"$group":
		{
		"_id":{"Cuenta Origen":"$Cuenta_Origen"},
		"total":{"$sum":1},
		"promedio":{"$avg":"$Monto"}
		}
	},
        {"$project":{"_id":1,"Transacciones realizadas":"$total","Promedio":"$promedio"}},
	{"$sort":{"Transacciones realizadas":-1}},
	{"$limit":25}]

pprint.pprint(list(collection.aggregate(pipeline)))
