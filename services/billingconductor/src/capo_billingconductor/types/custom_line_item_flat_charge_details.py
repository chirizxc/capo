"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemFlatChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_charge_value


class CustomLineItemFlatChargeDetails(TypedDict, closed=True):
    charge_value: "capo_billingconductor.types.custom_line_item_charge_value.CustomLineItemChargeValue"
    """<p>The custom line item's fixed charge value in USD.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemFlatChargeDetails) -> dict:
    out: dict = {}
    out["ChargeValue"] = (
        "NaN"
        if value["charge_value"] != value["charge_value"]
        else "Infinity"
        if value["charge_value"] == float("inf")
        else "-Infinity"
        if value["charge_value"] == float("-inf")
        else value["charge_value"]
    )
    return out


def deserialize_json(data: dict) -> CustomLineItemFlatChargeDetails:
    out: CustomLineItemFlatChargeDetails = {}  # type: ignore[typeddict-item]
    if data.get("ChargeValue") is not None:
        out["charge_value"] = float(data["ChargeValue"])
    else:
        raise DeserializationError(
            "CustomLineItemFlatChargeDetails.charge_value required"
        )
    return out
