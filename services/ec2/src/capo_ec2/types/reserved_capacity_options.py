"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reservation_type_list
    import capo_ec2.types.reserved_capacity_allocation_strategy
    import capo_ec2.types.reserved_capacity_fallback_options


class ReservedCapacityOptions(TypedDict, closed=True):
    allocation_strategy: NotRequired[
        "capo_ec2.types.reserved_capacity_allocation_strategy.ReservedCapacityAllocationStrategy"
    ]
    """<p>The strategy that determines the order in which EC2 Fleet launches instances across the reservation types that you specify. The only supported value is <code>prioritized</code>, which launches instances in the priority order that you specify in your launch template overrides. If you don't specify an allocation strategy, instances are launched in a random order.</p>"""
    reservation_types: NotRequired[
        "capo_ec2.types.reservation_type_list.ReservationTypeList"
    ]
    """<p>The types of Capacity Reservations used for fulfilling the EC2 Fleet request.</p>"""
    reserved_capacity_fallback_options: NotRequired[
        "capo_ec2.types.reserved_capacity_fallback_options.ReservedCapacityFallbackOptions"
    ]
    """<p>The fallback behavior for the EC2 Fleet when there is not enough reserved capacity available to meet the target capacity.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedCapacityOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_strategy" in value:
        import capo_ec2.types.reserved_capacity_allocation_strategy

        capo_ec2.types.reserved_capacity_allocation_strategy.serialize_ec2_query(
            value["allocation_strategy"], pairs, f"{key_prefix}AllocationStrategy"
        )
    if "reservation_types" in value:
        import capo_ec2.types.reservation_type_list

        capo_ec2.types.reservation_type_list.serialize_ec2_query(
            value["reservation_types"], pairs, f"{key_prefix}ReservationTypeSet"
        )
    if "reserved_capacity_fallback_options" in value:
        import capo_ec2.types.reserved_capacity_fallback_options

        capo_ec2.types.reserved_capacity_fallback_options.serialize_ec2_query(
            value["reserved_capacity_fallback_options"],
            pairs,
            f"{key_prefix}ReservedCapacityFallbackOptions",
        )


def deserialize_ec2_query(el: Element) -> ReservedCapacityOptions:
    out: ReservedCapacityOptions = {}  # type: ignore[typeddict-item]
    child_allocation_strategy = el.find("allocationStrategy")
    if child_allocation_strategy is not None:
        import capo_ec2.types.reserved_capacity_allocation_strategy

        out["allocation_strategy"] = (
            capo_ec2.types.reserved_capacity_allocation_strategy.deserialize_ec2_query(
                child_allocation_strategy
            )
        )
    child_reservation_types = el.find("reservationTypeSet")
    if child_reservation_types is not None:
        import capo_ec2.types.reservation_type_list

        out["reservation_types"] = (
            capo_ec2.types.reservation_type_list.deserialize_ec2_query(
                child_reservation_types
            )
        )
    child_reserved_capacity_fallback_options = el.find(
        "reservedCapacityFallbackOptions"
    )
    if child_reserved_capacity_fallback_options is not None:
        import capo_ec2.types.reserved_capacity_fallback_options

        out["reserved_capacity_fallback_options"] = (
            capo_ec2.types.reserved_capacity_fallback_options.deserialize_ec2_query(
                child_reserved_capacity_fallback_options
            )
        )
    return out
