"""Generated from Smithy shape ``com.amazonaws.m2#GdgDetailAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.integer
    import capo_m2.types.string50


class GdgDetailAttributes(TypedDict, closed=True):
    limit: "capo_m2.types.integer.Integer"
    """<p>The maximum number of generation data sets, up to 255, in a GDG.</p>"""
    roll_disposition: NotRequired["capo_m2.types.string50.String50"]
    """<p>The disposition of the data set in the catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GdgDetailAttributes) -> dict:
    out: dict = {}
    out["limit"] = value.get("limit", 0)
    if "roll_disposition" in value:
        out["rollDisposition"] = value["roll_disposition"]
    return out


def deserialize_json(data: dict) -> GdgDetailAttributes:
    out: GdgDetailAttributes = {}  # type: ignore[typeddict-item]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if data.get("rollDisposition") is not None:
        out["roll_disposition"] = data["rollDisposition"]
    return out
