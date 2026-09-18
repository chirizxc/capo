"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAPIAppSyncAuthSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__double
    import capo_amplifybackend.types.__string


class BackendAPIAppSyncAuthSettings(TypedDict, closed=True):
    cognito_user_pool_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The Amazon Cognito user pool ID, if Amazon Cognito was used as an authentication setting to access your data models.</p>"""
    description: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The API key description for API_KEY, if it was used as an authentication mechanism to access your data models.</p>"""
    expiration_time: NotRequired["capo_amplifybackend.types.__double.__double"]
    """<p>The API key expiration time for API_KEY, if it was used as an authentication mechanism to access your data models.</p>"""
    open_id_auth_ttl: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The expiry time for the OpenID authentication mechanism.</p>"""
    open_id_client_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The clientID for openID, if openID was used as an authentication setting to access your data models.</p>"""
    open_id_iat_ttl: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The expiry time for the OpenID authentication mechanism.</p>"""
    open_id_issue_url: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The openID issuer URL, if openID was used as an authentication setting to access your data models.</p>"""
    open_id_provider_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The OpenID provider name, if OpenID was used as an authentication mechanism to access your data models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAPIAppSyncAuthSettings) -> dict:
    out: dict = {}
    if "cognito_user_pool_id" in value:
        out["cognitoUserPoolId"] = value["cognito_user_pool_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "expiration_time" in value:
        out["expirationTime"] = (
            "NaN"
            if value["expiration_time"] != value["expiration_time"]
            else "Infinity"
            if value["expiration_time"] == float("inf")
            else "-Infinity"
            if value["expiration_time"] == float("-inf")
            else value["expiration_time"]
        )
    if "open_id_auth_ttl" in value:
        out["openIDAuthTTL"] = value["open_id_auth_ttl"]
    if "open_id_client_id" in value:
        out["openIDClientId"] = value["open_id_client_id"]
    if "open_id_iat_ttl" in value:
        out["openIDIatTTL"] = value["open_id_iat_ttl"]
    if "open_id_issue_url" in value:
        out["openIDIssueURL"] = value["open_id_issue_url"]
    if "open_id_provider_name" in value:
        out["openIDProviderName"] = value["open_id_provider_name"]
    return out


def deserialize_json(data: dict) -> BackendAPIAppSyncAuthSettings:
    out: BackendAPIAppSyncAuthSettings = {}  # type: ignore[typeddict-item]
    if data.get("cognitoUserPoolId") is not None:
        out["cognito_user_pool_id"] = data["cognitoUserPoolId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("expirationTime") is not None:
        out["expiration_time"] = float(data["expirationTime"])
    if data.get("openIDAuthTTL") is not None:
        out["open_id_auth_ttl"] = data["openIDAuthTTL"]
    if data.get("openIDClientId") is not None:
        out["open_id_client_id"] = data["openIDClientId"]
    if data.get("openIDIatTTL") is not None:
        out["open_id_iat_ttl"] = data["openIDIatTTL"]
    if data.get("openIDIssueURL") is not None:
        out["open_id_issue_url"] = data["openIDIssueURL"]
    if data.get("openIDProviderName") is not None:
        out["open_id_provider_name"] = data["openIDProviderName"]
    return out
