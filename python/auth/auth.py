from fastapi_users.authentication import CookieTransport, AuthenticationBackend

from config import JWT_SECRET_CODE

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="Auth_cookie",cookie_samesite="None", cookie_domain="localhost")

from fastapi_users.authentication import JWTStrategy

SECRET = JWT_SECRET_CODE

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=86400)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
