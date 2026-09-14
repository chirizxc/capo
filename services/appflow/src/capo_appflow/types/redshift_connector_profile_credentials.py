"""Generated from Smithy shape ``com.amazonaws.appflow#RedshiftConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.string


class RedshiftConnectorProfileCredentials(TypedDict, closed=True):
    username: NotRequired["capo_appflow.types.string.String"]
    """<p> The name of the user. </p>"""
    password: NotRequired["capo_appflow.types.password.Password"]
    """<p> The password that corresponds to the user name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "password" in value:
        out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> RedshiftConnectorProfileCredentials:
    out: RedshiftConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("password") is not None:
        out["password"] = data["password"]
    return out
