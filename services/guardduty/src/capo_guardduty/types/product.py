"""Generated from Smithy shape ``com.amazonaws.guardduty#Product``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class Product(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the product.</p>"""
    feature: NotRequired["capo_guardduty.types.string.String"]
    """<p>The specific feature within the product that produced the investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Product) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "feature" in value:
        out["feature"] = value["feature"]
    return out


def deserialize_json(data: dict) -> Product:
    out: Product = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("feature") is not None:
        out["feature"] = data["feature"]
    return out
