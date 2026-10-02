"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultOneDriveLocation``."""

from typing_extensions import NotRequired, TypedDict


class RetrievalResultOneDriveLocation(TypedDict, closed=True):
    url: NotRequired["str"]
    """<p>The OneDrive URL for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultOneDriveLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RetrievalResultOneDriveLocation:
    out: RetrievalResultOneDriveLocation = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    return out
