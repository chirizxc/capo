"""Generated from Smithy shape ``com.amazonaws.ec2#ModificationReservationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boxed_integer
    import capo_ec2.types.millisecond_date_time


class ModificationReservationUpdate(TypedDict, closed=True):
    new_commitment_end_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the commitment duration will expire after the modification, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    new_start_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date that the Capacity Reservation will have after the modification, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    new_commitment_duration: NotRequired["capo_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The commitment duration, in seconds, that the Capacity Reservation will have after the modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModificationReservationUpdate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "new_commitment_end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["new_commitment_end_date"], pairs, f"{key_prefix}NewCommitmentEndDate"
        )
    if "new_start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["new_start_date"], pairs, f"{key_prefix}NewStartDate"
        )
    if "new_commitment_duration" in value:
        pairs.append(
            (
                f"{key_prefix}NewCommitmentDuration",
                str(value["new_commitment_duration"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ModificationReservationUpdate:
    out: ModificationReservationUpdate = {}  # type: ignore[typeddict-item]
    child_new_commitment_end_date = el.find("newCommitmentEndDate")
    if child_new_commitment_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["new_commitment_end_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_new_commitment_end_date
            )
        )
    child_new_start_date = el.find("newStartDate")
    if child_new_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["new_start_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_new_start_date
            )
        )
    child_new_commitment_duration = el.find("newCommitmentDuration")
    if child_new_commitment_duration is not None:
        out["new_commitment_duration"] = int(child_new_commitment_duration.text or "")
    return out
