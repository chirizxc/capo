"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationAdjustmentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boxed_long
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class CapacityReservationAdjustmentDetails(TypedDict, closed=True):
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The start date that the Capacity Reservation will have after the adjustment.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end date that the Capacity Reservation will have after the adjustment.</p>"""
    commitment_end_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the commitment duration will expire after the adjustment.</p>"""
    end_date_type: NotRequired["capo_ec2.types.string.String"]
    """<p>Indicates the way in which the Capacity Reservation will end after the adjustment. Possible values are:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at the date and time given by <code>endDate</code>.</p> </li> </ul>"""
    commitment_duration: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The commitment duration, in seconds, that the Capacity Reservation will have after the adjustment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationAdjustmentDetails,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "commitment_end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["commitment_end_date"], pairs, f"{key_prefix}CommitmentEndDate"
        )
    if "end_date_type" in value:
        pairs.append((f"{key_prefix}EndDateType", str(value["end_date_type"])))
    if "commitment_duration" in value:
        pairs.append(
            (f"{key_prefix}CommitmentDuration", str(value["commitment_duration"]))
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationAdjustmentDetails:
    out: CapacityReservationAdjustmentDetails = {}  # type: ignore[typeddict-item]
    child_start_date = el.find("startDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_end_date = el.find("endDate")
    if child_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_commitment_end_date = el.find("commitmentEndDate")
    if child_commitment_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["commitment_end_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_commitment_end_date
            )
        )
    child_end_date_type = el.find("endDateType")
    if child_end_date_type is not None:
        out["end_date_type"] = str(child_end_date_type.text or "")
    child_commitment_duration = el.find("commitmentDuration")
    if child_commitment_duration is not None:
        out["commitment_duration"] = int(child_commitment_duration.text or "")
    return out
