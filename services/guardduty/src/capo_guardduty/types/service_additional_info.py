"""Generated from Smithy shape ``com.amazonaws.guardduty#ServiceAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class ServiceAdditionalInfo(TypedDict, closed=True):
    value: NotRequired["capo_guardduty.types.string.String"]
    """<p>This field specifies the value of the additional information.</p>"""
    type: NotRequired["capo_guardduty.types.string.String"]
    """<p>Describes the type of the additional information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAdditionalInfo) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ServiceAdditionalInfo:
    out: ServiceAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
