import logging
from typing import Awaitable, Callable

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader, OpenIdConnect
from keycloak import KeycloakError, KeycloakOpenID

from app.config import settings
from app.models.rail_user import RailUser

oidc = OpenIdConnect(
    openIdConnectUrl=settings.AIOD_KEYCLOAK.OIDC_URL,
    auto_error=False,
)

keycloak_openid = KeycloakOpenID(
    server_url=settings.AIOD_KEYCLOAK.SERVER_URL,
    client_id=settings.AIOD_KEYCLOAK.CLIENT_ID,
    client_secret_key=settings.AIOD_KEYCLOAK.CLIENT_SECRET,
    realm_name=settings.AIOD_KEYCLOAK.REALM,
    verify=True,
)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def get_current_user_token(token=Security(oidc)):
    return token


def get_current_user(
    required: bool,
    from_token: bool = True,
    from_api_key: bool = False,  # By default only for users authenticated through OIDC
) -> Callable[[str, str], Awaitable[dict | None]]:
    """
    Get the current user based on the provided token or API key (returns an async function).
    If both token and api_key are defined, the token will be used.
    
    Args:
        required (bool): Whether the user is required to be authenticated.
        from_token (bool): Whether the user can be authenticated through OIDC.
        from_api_key (bool): Whether the user can be authenticated through an API key.
    """
    
    async def _get_user(
        token: str = Security(oidc), api_key: str = Security(api_key_header)
    ) -> dict | None:
        """
        Get the current user based on the provided token or API key.
        If both token and api_key are defined, the token will be used.
        
        Args:
            token (str): The token provided by the user.
            api_key (str): The API key provided by the user.
        """
        if not from_token and not from_api_key:
            raise ValueError("Either from_token or from_api_key must be set to True")

        if not required and not token and not api_key:
            return None

        if from_token and token:
            return await _verify_token(token)
        if from_api_key and api_key:
            # TODO: Fetch userinfo based on user email from Keycloak
            # needs special role/rights in Keycloak for the client
            # In this way, this will return the same user info.
            user_obj = await RailUser.find_one({"api_key": api_key})
            if user_obj is not None:
                return user_obj.to_dict()
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid API key",
                    headers={"WWW-Authenticate": "Bearer"},
                )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="This endpoint requires authorization. You need to be logged in or provide an API key.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return _get_user


async def _verify_token(token: str) -> dict:
    try:
        token = token.replace("Bearer ", "")
        return keycloak_openid.userinfo(token)  # perform a request to keycloak
    except KeycloakError as e:
        error_msg = e.error_message
        error_detail = "Invalid authentication token"

        if isinstance(error_msg, bytes):
            error_msg = error_msg.decode("utf-8")

        if error_msg:
            error_detail = f"{error_detail}: '{error_msg}'"

        logging.error(error_detail)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=error_detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
