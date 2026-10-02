"""Generated from Smithy shape ``com.amazonaws.wafv2#MonetizeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.price_multiplier


class MonetizeAction(TypedDict, closed=True):
    price_multiplier: NotRequired["capo_wafv2.types.price_multiplier.PriceMultiplier"]
    """<p>An integer multiplier applied to the base price defined in the web ACL's <code>MonetizationConfig</code>. The effective price for the request is the base price multiplied by this value. Specify as a string. Valid values: 1 to 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetizeAction) -> dict:
    out: dict = {}
    if "price_multiplier" in value:
        out["PriceMultiplier"] = value["price_multiplier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonetizeAction:
    out: MonetizeAction = {}  # type: ignore[typeddict-item]
    if data.get("PriceMultiplier") is not None:
        out["price_multiplier"] = data["PriceMultiplier"]
    return out
