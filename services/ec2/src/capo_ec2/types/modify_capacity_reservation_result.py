"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyCapacityReservationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_adjustment_details
    import capo_ec2.types.capacity_reservation_adjustment_status

ModifyCapacityReservationResult = TypedDict(
    "ModifyCapacityReservationResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
        "adjustment_status": NotRequired[
            "capo_ec2.types.capacity_reservation_adjustment_status.CapacityReservationAdjustmentStatus"
        ],
        "adjustment_details": NotRequired[
            "capo_ec2.types.capacity_reservation_adjustment_details.CapacityReservationAdjustmentDetails"
        ],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyCapacityReservationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return" in value:
        pairs.append((f"{key_prefix}Return", "true" if value["return"] else "false"))
    if "adjustment_status" in value:
        import capo_ec2.types.capacity_reservation_adjustment_status

        capo_ec2.types.capacity_reservation_adjustment_status.serialize_ec2_query(
            value["adjustment_status"], pairs, f"{key_prefix}AdjustmentStatus"
        )
    if "adjustment_details" in value:
        import capo_ec2.types.capacity_reservation_adjustment_details

        capo_ec2.types.capacity_reservation_adjustment_details.serialize_ec2_query(
            value["adjustment_details"], pairs, f"{key_prefix}AdjustmentDetails"
        )


def deserialize_ec2_query(el: Element) -> ModifyCapacityReservationResult:
    out: ModifyCapacityReservationResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    child_adjustment_status = el.find("adjustmentStatus")
    if child_adjustment_status is not None:
        import capo_ec2.types.capacity_reservation_adjustment_status

        out["adjustment_status"] = (
            capo_ec2.types.capacity_reservation_adjustment_status.deserialize_ec2_query(
                child_adjustment_status
            )
        )
    child_adjustment_details = el.find("adjustmentDetails")
    if child_adjustment_details is not None:
        import capo_ec2.types.capacity_reservation_adjustment_details

        out["adjustment_details"] = (
            capo_ec2.types.capacity_reservation_adjustment_details.deserialize_ec2_query(
                child_adjustment_details
            )
        )
    return out
