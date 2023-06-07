import time
import uuid
from typing import Optional

from authlib.integrations.flask_client import OAuth
from authlib.jose import jwt as jose_jwt
from flask import current_app
from flask_jwt_extended import JWTManager
from models.users import User
from ops_api.ops.utils.authorization import AuthorizationGateway, BasicAuthorizationPrivider
from sqlalchemy import select

jwtMgr = JWTManager()
oauth = OAuth()
auth_gateway = AuthorizationGateway(BasicAuthorizationPrivider())


@jwtMgr.user_identity_loader
def user_identity_lookup(user: User) -> str:
    return user.oidc_id


@jwtMgr.user_lookup_loader
def user_lookup_callback(_jwt_header: dict, jwt_data: dict) -> Optional[User]:
    identity = jwt_data["sub"]
    stmt = select(User).where(User.oidc_id == identity)
    users = current_app.db_session.execute(stmt).all()
    if users and len(users) == 1:
        return users[0][0]


def create_oauth_jwt(
    key: Optional[str] = None,
    header: Optional[str] = None,
    payload: Optional[str] = None,
) -> str:
    """
    Returns an Access Token JWS from the configured OAuth Client
    :param key: OPTIONAL - Private Key used for encoding the JWS
    :param header: OPTIONAL - JWS Header containing algorithm type
    :param payload: OPTIONAL - Contains the JWS payload
    :return: JsonWebSignature
    """
    current_app.logger.debug("STARTING ----  creat_oauth_jwt")
    jwt_private_key = key or current_app.config.get("JWT_PRIVATE_KEY")
    if not jwt_private_key:
        raise NotImplementedError

    expire = current_app.config["JWT_ACCESS_TOKEN_EXPIRES"]
    current_app.logger.debug(f"expire={expire}")
    # client_id = current_app.config["AUTHLIB_OAUTH_CLIENTS"]["logingov"]["client_id"]
    _payload = payload or {
        "iss": current_app.config["AUTHLIB_OAUTH_CLIENTS"]["hhsams"]["client_id"],
        "sub": current_app.config["AUTHLIB_OAUTH_CLIENTS"]["hhsams"]["client_id"],
        "aud": "https://idp.int.identitysandbox.gov/api/openid_connect/token",
        "jti": str(uuid.uuid4()),
        "exp": int(time.time()) + expire.seconds,
    }
    _header = header or {"alg": "RS256"}
    jws = jose_jwt.encode(header=_header, payload=_payload, key=jwt_private_key)
    print(f"jws={jws}")
    return jws
