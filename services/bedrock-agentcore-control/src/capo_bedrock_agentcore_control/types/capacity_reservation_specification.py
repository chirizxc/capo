"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityReservationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_reservation_preference
    import capo_bedrock_agentcore_control.types.capacity_reservation_target


class CapacityReservationSpecification(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>The Capacity Reservation preference for the instances.</p>"""
    capacity_reservation_target: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_reservation_target.CapacityReservationTarget"
    ]
    """<p>The target Capacity Reservation or Capacity Reservation group for the instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityReservationSpecification) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        import capo_bedrock_agentcore_control.types.capacity_reservation_preference

        out["capacityReservationPreference"] = (
            capo_bedrock_agentcore_control.types.capacity_reservation_preference.serialize_json(
                value["capacity_reservation_preference"]
            )
        )
    if "capacity_reservation_target" in value:
        import capo_bedrock_agentcore_control.types.capacity_reservation_target

        out["capacityReservationTarget"] = (
            capo_bedrock_agentcore_control.types.capacity_reservation_target.serialize_json(
                value["capacity_reservation_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityReservationSpecification:
    out: CapacityReservationSpecification = {}  # type: ignore[typeddict-item]
    if data.get("capacityReservationPreference") is not None:
        import capo_bedrock_agentcore_control.types.capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            capo_bedrock_agentcore_control.types.capacity_reservation_preference.deserialize_json(
                data["capacityReservationPreference"]
            )
        )
    if data.get("capacityReservationTarget") is not None:
        import capo_bedrock_agentcore_control.types.capacity_reservation_target

        out["capacity_reservation_target"] = (
            capo_bedrock_agentcore_control.types.capacity_reservation_target.deserialize_json(
                data["capacityReservationTarget"]
            )
        )
    return out
