"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkInstanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class GetSolNetworkInstanceMetadata(TypedDict, closed=True):
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkInstanceMetadata) -> dict:
    out: dict = {}
    import capo_tnb._protocol.serialize

    out["createdAt"] = capo_tnb._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_tnb._protocol.serialize

    out["lastModified"] = capo_tnb._protocol.serialize.fmt_date_time(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolNetworkInstanceMetadata:
    out: GetSolNetworkInstanceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetSolNetworkInstanceMetadata.created_at required")
    if data.get("lastModified") is not None:
        import datetime

        out["last_modified"] = datetime.datetime.fromisoformat(
            data["lastModified"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "GetSolNetworkInstanceMetadata.last_modified required"
        )
    return out
