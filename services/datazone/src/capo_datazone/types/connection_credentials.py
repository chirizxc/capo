"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ConnectionCredentials(TypedDict, closed=True):
    access_key_id: NotRequired["str"]
    """<p>The access key ID of a connection.</p>"""
    secret_access_key: NotRequired["str"]
    """<p>The secret access key of a connection.</p>"""
    session_token: NotRequired["str"]
    """<p>The session token of a connection credentials.</p>"""
    expiration: NotRequired["datetime.datetime"]
    """<p>The expiration of the connection credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionCredentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["secretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["sessionToken"] = value["session_token"]
    if "expiration" in value:
        import capo_datazone._protocol.serialize

        out["expiration"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["expiration"]
        )
    return out


def deserialize_json(data: dict) -> ConnectionCredentials:
    out: ConnectionCredentials = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    if data.get("expiration") is not None:
        import datetime

        out["expiration"] = datetime.datetime.fromisoformat(
            data["expiration"].replace("Z", "+00:00")
        )
    return out
