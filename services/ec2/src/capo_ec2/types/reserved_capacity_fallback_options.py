"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityFallbackOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_capacity_fallback_market_type_list


class ReservedCapacityFallbackOptions(TypedDict, closed=True):
    market_types: NotRequired[
        "capo_ec2.types.reserved_capacity_fallback_market_type_list.ReservedCapacityFallbackMarketTypeList"
    ]
    """<p>The instance purchasing options to fall back to when the reserved capacity is not enough to meet the target capacity. The only supported value is <code>on-demand</code>, which launches On-Demand Instances to fulfill the remaining target capacity.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedCapacityFallbackOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "market_types" in value:
        import capo_ec2.types.reserved_capacity_fallback_market_type_list

        capo_ec2.types.reserved_capacity_fallback_market_type_list.serialize_ec2_query(
            value["market_types"], pairs, f"{key_prefix}MarketTypeSet"
        )


def deserialize_ec2_query(el: Element) -> ReservedCapacityFallbackOptions:
    out: ReservedCapacityFallbackOptions = {}  # type: ignore[typeddict-item]
    child_market_types = el.find("marketTypeSet")
    if child_market_types is not None:
        import capo_ec2.types.reserved_capacity_fallback_market_type_list

        out["market_types"] = (
            capo_ec2.types.reserved_capacity_fallback_market_type_list.deserialize_ec2_query(
                child_market_types
            )
        )
    return out
