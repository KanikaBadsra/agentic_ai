from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

SECRET_KEY = "nexusiq-secret"

ALGORITHM = "HS256"
security = HTTPBearer()

def get_current_user2(
    credentials=Depends(security)
):
    return verify_token(
        credentials.credentials
    )

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = verify_token(token)
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        return {
            "username": username,
            "role": role
        }
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
def create_access_token(username,role):
    payload = {
        "sub": username,
        "role": role
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token):

    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )