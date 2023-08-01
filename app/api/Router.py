from fastapi import APIRouter,HTTPException
from app.api.auth.validation import Validate
from app.api.models.model import person
from app.core.Config import settings
from app.api.database.sql import Database
from app.api.logs.logger import Log,levels


database = Database(settings.dbHost,
              settings.dbUsername,
              settings.dbPassword,
              settings.dbDatabase)
ValidationTool = Validate(database)
logger = Log(settings.logKey)

router = APIRouter()
@router.post("/people/register/")
async def registeruser(data:person):
    adminId, adminPassword = data.adminData.AdminId, data.adminData.AdminPassword
    success, query, logQ = ValidationTool.checkForAdmin(adminId, adminPassword)
    if not success:
        if logQ == 1:
            logger.log(levels.warning,
                            f"User Registration: Admin id entered '{data.adminData.AdminId}' does not exist")
        elif logQ == 2:
            logger.log(levels.warning,
                            f"User Registration: Password for Admin Id' {data.adminData.AdminId}' was incorrect")
        elif logQ == 3:
            logger.log(levels.warning,
                            f"User Registration: Id' {data.adminData.AdminId}' does not have admin permissions")
        raise HTTPException(400, detail=query)

    info = (data.id, data.firstName, data.middleName, data.lastName, data.gender, data.role, data.password)
    if database.checkusername(data.id) == False:
        raise HTTPException(400, detail="username already taken")
    logger.log(levels.warning, f"user '{data.id}' registered by '{data.adminData.AdminId}'")
    database.registerUser(info)

    raise HTTPException(200, detail="user registered")

@router.get("/people/info/")
async def getData(id=None, Password=None):
    if id == None:
        return database.getInfo("SELECT * FROM info")
    else:
        success, query = ValidationTool.authenticateUser(id, Password)
        if not success:
            logger.log(levels.warning,
                            f"Profile Viewing: Incorrect Password for id '{id}'")
            raise HTTPException(400, detail="Incorrect Password")
        logger.log(levels.warning,
                        f"Profile Viewing: Profile Viewed for id:'{id}' ")
        return database.getInfo(f"SELECT * FROM info WHERE id='{id}'")