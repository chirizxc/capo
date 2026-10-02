"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerSecurityFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_id


class ContainerSecurityFilters(TypedDict, closed=True):
    delivery_option_id: NotRequired[
        "capo_marketplace_catalog.types.resource_id.ResourceId"
    ]
    """<p>The unique ID of the delivery option whose Container Security assessments you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerSecurityFilters) -> dict:
    out: dict = {}
    if "delivery_option_id" in value:
        out["DeliveryOptionId"] = value["delivery_option_id"]
    return out


def deserialize_json(data: dict) -> ContainerSecurityFilters:
    out: ContainerSecurityFilters = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryOptionId") is not None:
        out["delivery_option_id"] = data["DeliveryOptionId"]
    return out
