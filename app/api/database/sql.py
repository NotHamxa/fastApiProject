import mysql.connector
from fastapi import HTTPException
class Database():
    def __init__(self,Host,User,Password,Database):
        self.db = mysql.connector.connect(host=Host,
                             user=User,
                             passwd=Password,
                             database=Database)
        self.cursor = self.db.cursor()
        self.basicFormula = "INSERT INTO info (id,FirstName,MiddleName,LastName,Gender,role,password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    def getInfo(self,argument):
        self.cursor.execute(argument)
        x=self.cursor.fetchall()
        return x
    def registerUser(self,details:tuple):
        self.cursor.execute(self.basicFormula,details)
        self.db.commit()
    def checkusername(self,name):

        self.cursor.execute(f"SELECT firstname FROM info WHERE id='{name}'")
        x=self.cursor.fetchall()
        if x == []:
            return True
        else:
            return False





