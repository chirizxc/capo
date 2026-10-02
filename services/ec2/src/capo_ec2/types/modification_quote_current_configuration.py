"""Generated from Smithy shape ``com.amazonaws.ec2#ModificationQuoteCurrentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class ModificationQuoteCurrentConfiguration(TypedDict, closed=True):
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Reservation.</p>"""
    reservation_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the Capacity Reservation.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The start date that the Capacity Reservation has before the quoted modification is applied.</p>"""
    original_start_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date that the Capacity Reservation was originally requested with. This value does not change when you push out the start date.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModificationQuoteCurrentConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "reservation_state" in value:
        pairs.append((f"{key_prefix}ReservationState", str(value["reservation_state"])))
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "original_start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["original_start_date"], pairs, f"{key_prefix}OriginalStartDate"
        )


def deserialize_ec2_query(el: Element) -> ModificationQuoteCurrentConfiguration:
    out: ModificationQuoteCurrentConfiguration = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("instanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_reservation_state = el.find("reservationState")
    if child_reservation_state is not None:
        out["reservation_state"] = str(child_reservation_state.text or "")
    child_start_date = el.find("startDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_original_start_date = el.find("originalStartDate")
    if child_original_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["original_start_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_original_start_date
            )
        )
    return out
