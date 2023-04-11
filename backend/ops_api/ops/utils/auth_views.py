from typing import Union

import requests
from flask import Response, current_app, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from models.events import OpsEventType
from ops_api.ops.utils.auth import create_oauth_jwt, oauth
from ops_api.ops.utils.events import OpsEventHandler
from ops_api.ops.utils.response import make_response_with_headers
from ops_api.ops.utils.user import process_user


def login() -> Union[Response, tuple[str, int]]:
    auth_code = request.json.get("code")
    current_app.logger.debug(f"Got an OIDC request with the code of {auth_code}")

    with OpsEventHandler(OpsEventType.LOGIN_ATTEMPT) as la:
        token, user_data = _get_token_and_user_data_from_oauth_provider(auth_code)

        access_token, refresh_token, user = _get_token_and_user_data_from_internal_auth(user_data)

        la.metadata.update(
            {
                "user": user.to_dict(),
                "access_token": access_token,
                "refresh_token": refresh_token,
                "logingov_token": token,
            }
        )

        return make_response_with_headers({"access_token": access_token, "refresh_token": refresh_token})


def _get_token_and_user_data_from_internal_auth(user_data):
    # Generate internal backend-JWT
    # - user meta data
    # - endpoints validate backend-JWT
    #   - refesh - within 15 min - also include a call to login.gov /refresh
    #   - invalid JWT
    # - create backend-JWT endpoints /refesh /validate (drf-simplejwt)
    # See if user exists
    user = process_user(user_data)  # Refactor me
    # TODO
    # Do we want to embed the user's roles or permissions in the scope: [read write]?
    # The next two tokens are specific to our backend API, these are used for our API
    # authZ, given a valid login from the prior AuthN steps above.
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    return access_token, refresh_token, user


def _get_token_and_user_data_from_oauth_provider(auth_code: str):
    authlib_client_config = current_app.config["AUTHLIB_OAUTH_CLIENTS"]["logingov"]
    oauth.register(
        "logingov",
        client_id=authlib_client_config["client_id"],
        server_metadata_url=authlib_client_config["server_metadata_url"],
        client_kwargs=authlib_client_config["client_kwargs"],
    )
    token = oauth.logingov.fetch_access_token(
        "",
        client_assertion=create_oauth_jwt(),
        client_assertion_type="urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        grant_type="authorization_code",
        code=auth_code,
    )
    header = {"Authorization": f'Bearer {token["access_token"]}'}
    user_data = requests.get(
        authlib_client_config["user_info_url"],
        headers=header,
    ).json()
    return token, user_data


# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@jwt_required(refresh=True)
def refresh() -> Response:
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return make_response_with_headers({"access_token": access_token})
