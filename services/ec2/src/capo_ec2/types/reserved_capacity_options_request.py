"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_capacity_reservation_target_request
    import capo_ec2.types.reservation_type_list_request
    import capo_ec2.types.reserved_capacity_allocation_strategy
    import capo_ec2.types.reserved_capacity_fallback_options_request


class ReservedCapacityOptionsRequest(TypedDict, closed=True):
    allocation_strategy: NotRequired[
        "capo_ec2.types.reserved_capacity_allocation_strategy.ReservedCapacityAllocationStrategy"
    ]
    """<p>The strategy that determines the order in which EC2 Fleet launches instances across the reservation types that you specify. The only supported value is <code>prioritized</code>, which launches instances in the priority order that you specify in your launch template overrides. If you don't specify an allocation strategy, instances are launched in a random order.</p>"""
    reservation_types: NotRequired[
        "capo_ec2.types.reservation_type_list_request.ReservationTypeListRequest"
    ]
    """<p>The types of Capacity Reservations to use for fulfilling the EC2 Fleet request. This is an ordered list: EC2 Fleet attempts to launch instances into each Capacity Reservation type in the order that you specify them before moving on to the next type.</p>"""
    capacity_reservation_target: NotRequired[
        "capo_ec2.types.fleet_capacity_reservation_target_request.FleetCapacityReservationTargetRequest"
    ]
    """<p>The Capacity Reservations or Capacity Reservation Resource Groups to use for fulfilling the EC2 Fleet request. You can specify Capacity Reservation IDs or a Capacity Reservation Resource Group ARN, but not both.</p>"""
    reserved_capacity_fallback_options: NotRequired[
        "capo_ec2.types.reserved_capacity_fallback_options_request.ReservedCapacityFallbackOptionsRequest"
    ]
    """<p>The fallback behavior for the EC2 Fleet when there is not enough reserved capacity available to meet the target capacity. This member takes a <code>ReservedCapacityFallbackOptionsRequest</code> structure, in which you set <code>MarketTypes</code> to the instance purchasing options to fall back to.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedCapacityOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_strategy" in value:
        import capo_ec2.types.reserved_capacity_allocation_strategy

        capo_ec2.types.reserved_capacity_allocation_strategy.serialize_ec2_query(
            value["allocation_strategy"], pairs, f"{key_prefix}AllocationStrategy"
        )
    if "reservation_types" in value:
        import capo_ec2.types.reservation_type_list_request

        capo_ec2.types.reservation_type_list_request.serialize_ec2_query(
            value["reservation_types"], pairs, f"{key_prefix}ReservationType"
        )
    if "capacity_reservation_target" in value:
        import capo_ec2.types.fleet_capacity_reservation_target_request

        capo_ec2.types.fleet_capacity_reservation_target_request.serialize_ec2_query(
            value["capacity_reservation_target"],
            pairs,
            f"{key_prefix}CapacityReservationTarget",
        )
    if "reserved_capacity_fallback_options" in value:
        import capo_ec2.types.reserved_capacity_fallback_options_request

        capo_ec2.types.reserved_capacity_fallback_options_request.serialize_ec2_query(
            value["reserved_capacity_fallback_options"],
            pairs,
            f"{key_prefix}ReservedCapacityFallbackOptions",
        )


def deserialize_ec2_query(el: Element) -> ReservedCapacityOptionsRequest:
    out: ReservedCapacityOptionsRequest = {}  # type: ignore[typeddict-item]
    child_allocation_strategy = el.find("AllocationStrategy")
    if child_allocation_strategy is not None:
        import capo_ec2.types.reserved_capacity_allocation_strategy

        out["allocation_strategy"] = (
            capo_ec2.types.reserved_capacity_allocation_strategy.deserialize_ec2_query(
                child_allocation_strategy
            )
        )
    child_reservation_types = el.find("ReservationType")
    if child_reservation_types is not None:
        import capo_ec2.types.reservation_type_list_request

        out["reservation_types"] = (
            capo_ec2.types.reservation_type_list_request.deserialize_ec2_query(
                child_reservation_types
            )
        )
    child_capacity_reservation_target = el.find("CapacityReservationTarget")
    if child_capacity_reservation_target is not None:
        import capo_ec2.types.fleet_capacity_reservation_target_request

        out["capacity_reservation_target"] = (
            capo_ec2.types.fleet_capacity_reservation_target_request.deserialize_ec2_query(
                child_capacity_reservation_target
            )
        )
    child_reserved_capacity_fallback_options = el.find(
        "ReservedCapacityFallbackOptions"
    )
    if child_reserved_capacity_fallback_options is not None:
        import capo_ec2.types.reserved_capacity_fallback_options_request

        out["reserved_capacity_fallback_options"] = (
            capo_ec2.types.reserved_capacity_fallback_options_request.deserialize_ec2_query(
                child_reserved_capacity_fallback_options
            )
        )
    return out
