from jose import JWSError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
#Secret_Key
#Algorithm
#Expiration Time

ALGORITHM = "HS256"
SECRET_KEY = "shzc3^d*cjla3&908.//3ac;'s345'sd903jkrd393/zcv033r5a"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
    

