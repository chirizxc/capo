"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityReservationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_reservation_id
    import capo_bedrock_agentcore_control.types.capacity_reservation_resource_group_arn


class CapacityReservationTarget(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation in which to run the instances.</p>"""
    capacity_reservation_resource_group_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_reservation_resource_group_arn.CapacityReservationResourceGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Capacity Reservation resource group in which to run the instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityReservationTarget) -> dict:
    out: dict = {}
    if "capacity_reservation_id" in value:
        out["capacityReservationId"] = value["capacity_reservation_id"]
    if "capacity_reservation_resource_group_arn" in value:
        out["capacityReservationResourceGroupArn"] = value[
            "capacity_reservation_resource_group_arn"
        ]
    return out


def deserialize_json(data: dict) -> CapacityReservationTarget:
    out: CapacityReservationTarget = {}  # type: ignore[typeddict-item]
    if data.get("capacityReservationId") is not None:
        out["capacity_reservation_id"] = data["capacityReservationId"]
    if data.get("capacityReservationResourceGroupArn") is not None:
        out["capacity_reservation_resource_group_arn"] = data[
            "capacityReservationResourceGroupArn"
        ]
    return out
