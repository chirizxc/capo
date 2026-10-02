"""Generated from Smithy shape ``com.amazonaws.batch#CapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class CapacityReservationRequest(TypedDict, closed=True):
    reservation_group_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capacity reservation group to target.</p>"""
    reservation_preference: NotRequired["capo_batch.types.string.String"]
    """<p>The capacity reservation preference. Valid values:</p> <ul> <li> <p> <code>RESERVATIONS_ONLY</code> — Use only capacity reservations.</p> </li> <li> <p> <code>RESERVATIONS_FIRST</code> — Prefer capacity reservations but fall back to On-Demand if unavailable.</p> </li> <li> <p> <code>RESERVATIONS_EXCLUDED</code> — Do not use capacity reservations.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityReservationRequest) -> dict:
    out: dict = {}
    if "reservation_group_arn" in value:
        out["reservationGroupArn"] = value["reservation_group_arn"]
    if "reservation_preference" in value:
        out["reservationPreference"] = value["reservation_preference"]
    return out


def deserialize_json(data: dict) -> CapacityReservationRequest:
    out: CapacityReservationRequest = {}  # type: ignore[typeddict-item]
    if data.get("reservationGroupArn") is not None:
        out["reservation_group_arn"] = data["reservationGroupArn"]
    if data.get("reservationPreference") is not None:
        out["reservation_preference"] = data["reservationPreference"]
    return out
