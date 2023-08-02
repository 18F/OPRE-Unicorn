import time
import uuid
from enum import Enum, auto
from functools import wraps
from typing import Callable, Optional

from authlib.integrations.flask_client import OAuth
from authlib.jose import jwt as jose_jwt
from flask import Response, current_app
from flask_jwt_extended import JWTManager, get_current_user, get_jwt_identity, jwt_required
from models.users import User
from ops_api.ops.utils.authorization import AuthorizationGateway, BasicAuthorizationPrivider
from ops_api.ops.utils.response import make_response_with_headers
from sqlalchemy import select

jwtMgr = JWTManager()
oauth = OAuth()
auth_gateway = AuthorizationGateway(BasicAuthorizationPrivider())


class PermissionType(Enum):
    DELETE = auto()
    GET = auto()
    PATCH = auto()
    POST = auto()
    PUT = auto()


class Permission(Enum):
    AGREEMENT = auto()
    BUDGET_LINE_ITEM = auto()
    CAN = auto()
    DIVISION = auto()
    HISTORY = auto()
    NOTIFICATION = auto()
    PORTFOLIO = auto()
    RESEARCH_PROJECT = auto()
    USER = auto()


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
    return None


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
    jwt_private_key = key or current_app.config.get("JWT_PRIVATE_KEY")
    if not jwt_private_key:
        raise NotImplementedError

    expire = current_app.config["JWT_ACCESS_TOKEN_EXPIRES"]

    # client_id = current_app.config["AUTHLIB_OAUTH_CLIENTS"]["logingov"]["client_id"]
    _payload = payload or {
        "iss": current_app.config["AUTHLIB_OAUTH_CLIENTS"]["logingov"]["client_id"],
        "sub": current_app.config["AUTHLIB_OAUTH_CLIENTS"]["logingov"]["client_id"],
        "aud": "https://idp.int.identitysandbox.gov/api/openid_connect/token",
        "jti": str(uuid.uuid4()),
        "exp": int(time.time()) + expire.seconds,
    }
    _header = header or {"alg": "RS256"}
    jws = jose_jwt.encode(header=_header, payload=_payload, key=jwt_private_key)
    return jws


class is_authorized:
    def __init__(
        self,
        permission_type: PermissionType,
        permission: Permission,
        extra_check: Optional[Callable[..., bool]] = None,
        groups: Optional[list[str]] = None,
    ) -> None:
        self.permission_type = permission_type
        self.permission = permission
        self.extra_check = extra_check
        self.groups = groups

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs) -> Response:
            identity = get_jwt_identity()
            is_authorized = auth_gateway.is_authorized(identity, f"{self.permission_type}_{self.permission}".upper())
            response: Optional[Response] = None
            if is_authorized:

                extra_valid: Optional[bool] = None
                auth_group: Optional[bool] = None
                if self.extra_check is not None:
                    try:
                        extra_valid = self.extra_check(*args, **kwargs)
                    except AttributeError:
                        return make_response_with_headers({}, 400)

                if self.groups is not None:
                    user = get_current_user()
                    if set(self.groups) & {g.name for g in user.groups}:
                        auth_group = True
                    else:
                        auth_group = False

                if (
                    (extra_valid is None and auth_group is None) or
                    (extra_valid is None and auth_group) or
                    (auth_group is None and extra_valid) or
                    (extra_valid is not None and auth_group is not None and (extra_valid or auth_group))
                ):
                    response = func(*args, **kwargs)

            if response is None:
                response = make_response_with_headers({}, 401)

            return response

        return wrapper
