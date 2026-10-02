"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WebNotificationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.browser_id
    import capo_connectcampaignsv2.types.session_id


class WebNotificationContext(TypedDict, closed=True):
    session_id: NotRequired["capo_connectcampaignsv2.types.session_id.SessionId"]
    browser_id: NotRequired["capo_connectcampaignsv2.types.browser_id.BrowserId"]


# --- restJson1 ser/de ---
def serialize_json(value: WebNotificationContext) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "browser_id" in value:
        out["browserId"] = value["browser_id"]
    return out


def deserialize_json(data: dict) -> WebNotificationContext:
    out: WebNotificationContext = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("browserId") is not None:
        out["browser_id"] = data["browserId"]
    return out
