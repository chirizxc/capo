"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultGoogleDriveLocation``."""

from typing_extensions import NotRequired, TypedDict


class RetrievalResultGoogleDriveLocation(TypedDict, closed=True):
    url: NotRequired["str"]
    """<p>The Google Drive URL for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultGoogleDriveLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RetrievalResultGoogleDriveLocation:
    out: RetrievalResultGoogleDriveLocation = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    return out
