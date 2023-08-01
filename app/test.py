from api.database.sql import Database


db = Database("mydatabase2.mysql.database.azure.com","nothamxa","Database123","people")

person = ("NotHamxa","Hamza","","Ahmed","male","admin","1234")
db.registerUser(person)