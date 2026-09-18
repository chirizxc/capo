"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemPercentageChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_percentage_charge_value


class ListCustomLineItemPercentageChargeDetails(TypedDict, closed=True):
    percentage_value: "capo_billingconductor.types.custom_line_item_percentage_charge_value.CustomLineItemPercentageChargeValue"
    """<p> The custom line item's percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemPercentageChargeDetails) -> dict:
    out: dict = {}
    out["PercentageValue"] = (
        "NaN"
        if value["percentage_value"] != value["percentage_value"]
        else "Infinity"
        if value["percentage_value"] == float("inf")
        else "-Infinity"
        if value["percentage_value"] == float("-inf")
        else value["percentage_value"]
    )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemPercentageChargeDetails:
    out: ListCustomLineItemPercentageChargeDetails = {}  # type: ignore[typeddict-item]
    if data.get("PercentageValue") is not None:
        out["percentage_value"] = float(data["PercentageValue"])
    else:
        raise DeserializationError(
            "ListCustomLineItemPercentageChargeDetails.percentage_value required"
        )
    return out
