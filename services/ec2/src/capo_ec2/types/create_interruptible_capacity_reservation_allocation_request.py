"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInterruptibleCapacityReservationAllocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.zero_size_preference


class CreateInterruptibleCapacityReservationAllocationRequest(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation from which to create the interruptible Capacity Reservation. Your Capacity Reservation must be in active state with no end date set and have available capacity for allocation. </p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> The number of instances to allocate from your source reservation. You can only allocate available instances (also called unused capacity). </p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> The tags to apply to the interruptible Capacity Reservation during creation. </p>"""
    zero_size_preference: NotRequired[
        "capo_ec2.types.zero_size_preference.ZeroSizePreference"
    ]
    """<p> Specifies the behavior for the interruptible Capacity Reservation when you reduce its allocation to zero instances. Specify <code>retain</code> to keep the interruptible Capacity Reservation active at zero capacity so that you can allocate instances to it again later. Specify <code>default</code> to cancel the interruptible Capacity Reservation and return the capacity to your source Capacity Reservation. The default value is <code>default</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInterruptibleCapacityReservationAllocationRequest,
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
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "zero_size_preference" in value:
        import capo_ec2.types.zero_size_preference

        capo_ec2.types.zero_size_preference.serialize_ec2_query(
            value["zero_size_preference"], pairs, f"{key_prefix}ZeroSizePreference"
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateInterruptibleCapacityReservationAllocationRequest:
    out: CreateInterruptibleCapacityReservationAllocationRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_zero_size_preference = el.find("ZeroSizePreference")
    if child_zero_size_preference is not None:
        import capo_ec2.types.zero_size_preference

        out["zero_size_preference"] = (
            capo_ec2.types.zero_size_preference.deserialize_ec2_query(
                child_zero_size_preference
            )
        )
    return out
