
class Validate():
    def __init__(self,db):
        self.database = db
    def authenticateUser(self,id,password):

        if self.database.checkusername(id) == True:
            query="username does not exist"
            return False,query
        Password = self.database.getInfo(f"SELECT password FROM info WHERE id='{id}'")
        if password != Password[0][0]:
            query="Incorrect password"
            return False,query
        return True,""

    def checkForAdmin(self,id,password):
        loggerQuery=""
        if self.database.checkusername(id) == True:
            query="Admin Username Does not exist"
            return False,query,1
        Data = self.database.getInfo(f"SELECT password,role FROM info WHERE id='{id}'")

        if password != Data[0][0]:
            query="Password for 'Admin Id' was incorrect"
            return False, query,2
        if Data[0][1]!="admin":
            query="User does not have admin permissions"
            return False,query,3


        return True,"",0