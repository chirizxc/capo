"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourceProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ResourceProperty(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of this property of the resource.</p>"""
    last_reported_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the information about this resource property was last updated.</p>"""
    data: NotRequired["object"]
    """<p>Details about this property. The content of this field is a JSON object that varies based on the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceProperty) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "last_reported_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["LastReportedAt"] = (
            capo_resource_explorer_2._protocol.serialize.fmt_date_time(
                value["last_reported_at"]
            )
        )
    if "data" in value:
        out["Data"] = value["data"]
    return out


def deserialize_json(data: dict) -> ResourceProperty:
    out: ResourceProperty = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LastReportedAt") is not None:
        import datetime

        out["last_reported_at"] = datetime.datetime.fromisoformat(
            data["LastReportedAt"].replace("Z", "+00:00")
        )
    if data.get("Data") is not None:
        out["data"] = data["Data"]
    return out
