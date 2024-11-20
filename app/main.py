from datetime import datetime, timedelta
from jose import ExpiredSignatureError, JWTError, jwt

SECRET_AT_KEY = "your_secret_key" 
SECRET_RT_KEY = "your_secret_key" 
ALGORITHM = "HS256"
ISSUER = "Duy"

ACCESS_TOKEN_EXPIRATION_TIME = datetime.utc(datetime.timezone.utc) + timedelta(hours=1)
REFRESH_TOKEN_EXPIRATION_TIME = datetime.utc(datetime.timezone.utc) + timedelta(weeks=1)

def create_access_token(user_account: str) -> str:
    """
    Tạo access token với JWT
    :param user_account: Tài khoản người dùng (subject)
    :return: JWT access token
    """
    payload = {
        "iss": ISSUER,  # Issuer
        "sub": user_account,  # Subject (user account)
        "exp": ACCESS_TOKEN_EXPIRATION_TIME,  # Expiration time
        "iat": datetime.utc(datetime.timezone.utc)  # Issued at time
    }
    
    token = jwt.encode(payload, ACCESS_TOKEN_EXPIRATION_TIME, algorithm=ALGORITHM)
    return token

# user_account = "example_user"
# access_token = create_access_token(user_account)
# print("Access Token:", access_token)


def verify_access_token(token: str):
    """
    Xác thực tính hợp lệ của access token
    :param token: JWT access token
    :return: Payload của token nếu hợp lệ
    :raises: ValueError nếu token không hợp lệ
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        if payload.get("iss") != ISSUER:
            raise JWTError("Invalid issuer")
        return payload
    except ExpiredSignatureError:
        raise ValueError("Token has expired")
    except JWTError as e:
        raise ValueError(f"Invalid token: {e}")

try:
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXkiLCJzdWIiOiJleGFtcGxlX3VzZXIiLCJleHAiOjE3MzIxMDQyMjgsImlhdCI6MTczMjEwMDYyOH0.FPv66NapYTwcH7nuzrtpccpMKxWnh2y7O0XjvjIKx2g"  # Thay bằng token của bạn
    payload = verify_access_token(token)
    print("Token is valid:", payload)
except ValueError as e:
    print("Token verification failed:", e)