"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservationTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_id_set
    import capo_ec2.types.capacity_reservation_resource_group_arn_set


class FleetCapacityReservationTargetRequest(TypedDict, closed=True):
    capacity_reservation_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The IDs of the Capacity Reservations in which to launch the instances.</p>"""
    capacity_reservation_resource_group_arns: NotRequired[
        "capo_ec2.types.capacity_reservation_resource_group_arn_set.CapacityReservationResourceGroupArnSet"
    ]
    """<p>The ARNs of the Capacity Reservation Resource Groups in which to launch the instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetCapacityReservationTargetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_ids" in value:
        import capo_ec2.types.capacity_reservation_id_set

        capo_ec2.types.capacity_reservation_id_set.serialize_ec2_query(
            value["capacity_reservation_ids"],
            pairs,
            f"{key_prefix}CapacityReservationId",
        )
    if "capacity_reservation_resource_group_arns" in value:
        import capo_ec2.types.capacity_reservation_resource_group_arn_set

        capo_ec2.types.capacity_reservation_resource_group_arn_set.serialize_ec2_query(
            value["capacity_reservation_resource_group_arns"],
            pairs,
            f"{key_prefix}CapacityReservationResourceGroupArn",
        )


def deserialize_ec2_query(el: Element) -> FleetCapacityReservationTargetRequest:
    out: FleetCapacityReservationTargetRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_ids = el.find("CapacityReservationId")
    if child_capacity_reservation_ids is not None:
        import capo_ec2.types.capacity_reservation_id_set

        out["capacity_reservation_ids"] = (
            capo_ec2.types.capacity_reservation_id_set.deserialize_ec2_query(
                child_capacity_reservation_ids
            )
        )
    child_capacity_reservation_resource_group_arns = el.find(
        "CapacityReservationResourceGroupArn"
    )
    if child_capacity_reservation_resource_group_arns is not None:
        import capo_ec2.types.capacity_reservation_resource_group_arn_set

        out["capacity_reservation_resource_group_arns"] = (
            capo_ec2.types.capacity_reservation_resource_group_arn_set.deserialize_ec2_query(
                child_capacity_reservation_resource_group_arns
            )
        )
    return out
