"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateInterruptibleCapacityReservationAllocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.integer
    import capo_ec2.types.zero_size_preference


class UpdateInterruptibleCapacityReservationAllocationRequest(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation containing the interruptible allocation to modify. </p>"""
    target_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> The new number of instances to allocate. Enter a higher number to add more capacity to share, or a lower number to reclaim capacity to your source Capacity Reservation. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. </p>"""
    zero_size_preference: NotRequired[
        "capo_ec2.types.zero_size_preference.ZeroSizePreference"
    ]
    """<p> Specifies the updated behavior for the interruptible Capacity Reservation when you reduce its allocation to zero instances. Specify <code>retain</code> to keep the interruptible Capacity Reservation active at zero capacity so that you can allocate instances to it again later. Specify <code>default</code> to cancel the interruptible Capacity Reservation and return the capacity to your source Capacity Reservation. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateInterruptibleCapacityReservationAllocationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "target_instance_count" in value:
        pairs.append(
            (f"{key_prefix}TargetInstanceCount", str(value["target_instance_count"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "zero_size_preference" in value:
        import capo_ec2.types.zero_size_preference

        capo_ec2.types.zero_size_preference.serialize_ec2_query(
            value["zero_size_preference"], pairs, f"{key_prefix}ZeroSizePreference"
        )


def deserialize_ec2_query(
    el: Element,
) -> UpdateInterruptibleCapacityReservationAllocationRequest:
    out: UpdateInterruptibleCapacityReservationAllocationRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_target_instance_count = el.find("TargetInstanceCount")
    if child_target_instance_count is not None:
        out["target_instance_count"] = int(child_target_instance_count.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_zero_size_preference = el.find("ZeroSizePreference")
    if child_zero_size_preference is not None:
        import capo_ec2.types.zero_size_preference

        out["zero_size_preference"] = (
            capo_ec2.types.zero_size_preference.deserialize_ec2_query(
                child_zero_size_preference
            )
        )
    return out
