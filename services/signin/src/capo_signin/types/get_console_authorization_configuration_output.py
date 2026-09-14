"""Generated from Smithy shape ``com.amazonaws.signin#GetConsoleAuthorizationConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.target_id


class GetConsoleAuthorizationConfigurationOutput(TypedDict, closed=True):
    target_id: "capo_signin.types.target_id.TargetId"
    """Target account identifier"""
    scope: "str"
    """Authorization scope"""
    console_authorization_enabled: "bool"
    """Whether console authorization is enabled"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConsoleAuthorizationConfigurationOutput) -> dict:
    out: dict = {}
    out["targetId"] = value["target_id"]
    out["scope"] = value["scope"]
    out["consoleAuthorizationEnabled"] = value["console_authorization_enabled"]
    return out


def deserialize_json(data: dict) -> GetConsoleAuthorizationConfigurationOutput:
    out: GetConsoleAuthorizationConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError(
            "GetConsoleAuthorizationConfigurationOutput.target_id required"
        )
    if data.get("scope") is not None:
        out["scope"] = data["scope"]
    else:
        raise DeserializationError(
            "GetConsoleAuthorizationConfigurationOutput.scope required"
        )
    if data.get("consoleAuthorizationEnabled") is not None:
        out["console_authorization_enabled"] = data["consoleAuthorizationEnabled"]
    else:
        raise DeserializationError(
            "GetConsoleAuthorizationConfigurationOutput.console_authorization_enabled required"
        )
    return out
