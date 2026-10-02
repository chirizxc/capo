"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.product
    import capo_guardduty.types.string


class InvestigationMetadata(TypedDict, closed=True):
    version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the investigation engine that produced the results.</p>"""
    product: NotRequired["capo_guardduty.types.product.Product"]
    """<p>Information about the product that produced the investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationMetadata) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "product" in value:
        import capo_guardduty.types.product

        out["product"] = capo_guardduty.types.product.serialize_json(value["product"])
    return out


def deserialize_json(data: dict) -> InvestigationMetadata:
    out: InvestigationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("product") is not None:
        import capo_guardduty.types.product

        out["product"] = capo_guardduty.types.product.deserialize_json(data["product"])
    return out
