"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorOAuthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.auth_code
    import capo_appflow.types.code_verifier
    import capo_appflow.types.redirect_uri


class ConnectorOAuthRequest(TypedDict, closed=True):
    auth_code: NotRequired["capo_appflow.types.auth_code.AuthCode"]
    """<p> The code provided by the connector when it has been authenticated via the connected app. </p>"""
    redirect_uri: NotRequired["capo_appflow.types.redirect_uri.RedirectUri"]
    """<p> The URL to which the authentication server redirects the browser after authorization has been granted. </p>"""
    code_verifier: NotRequired["capo_appflow.types.code_verifier.CodeVerifier"]
    """<p> The code verifier used in the PKCE (Proof Key for Code Exchange) OAuth flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOAuthRequest) -> dict:
    out: dict = {}
    if "auth_code" in value:
        out["authCode"] = value["auth_code"]
    if "redirect_uri" in value:
        out["redirectUri"] = value["redirect_uri"]
    if "code_verifier" in value:
        out["codeVerifier"] = value["code_verifier"]
    return out


def deserialize_json(data: dict) -> ConnectorOAuthRequest:
    out: ConnectorOAuthRequest = {}  # type: ignore[typeddict-item]
    if data.get("authCode") is not None:
        out["auth_code"] = data["authCode"]
    if data.get("redirectUri") is not None:
        out["redirect_uri"] = data["redirectUri"]
    if data.get("codeVerifier") is not None:
        out["code_verifier"] = data["codeVerifier"]
    return out
