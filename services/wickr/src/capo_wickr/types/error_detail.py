"""Generated from Smithy shape ``com.amazonaws.wickr#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class ErrorDetail(TypedDict, closed=True):
    field: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The name of the field that contains an error or warning.</p>"""
    reason: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A detailed description of the error or warning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
