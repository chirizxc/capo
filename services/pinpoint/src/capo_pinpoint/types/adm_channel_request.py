"""Generated from Smithy shape ``com.amazonaws.pinpoint#ADMChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__string


class ADMChannelRequest(TypedDict, closed=True):
    client_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Client ID that you received from Amazon to send messages by using ADM.</p>"""
    client_secret: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Client Secret that you received from Amazon to send messages by using ADM.</p>"""
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the ADM channel for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ADMChannelRequest) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ADMChannelRequest:
    out: ADMChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
