"""Generated from Smithy shape ``com.amazonaws.groundstation#GetMinuteUsageResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetMinuteUsageResponse(TypedDict, closed=True):
    is_reserved_minutes_customer: NotRequired["bool"]
    """<p>Returns whether or not an account has signed up for the reserved minutes pricing plan, specific to the month being requested.</p>"""
    total_reserved_minute_allocation: NotRequired["int"]
    """<p>Total number of reserved minutes allocated, specific to the month being requested.</p>"""
    upcoming_minutes_scheduled: NotRequired["int"]
    """<p>Upcoming minutes scheduled for an account, specific to the month being requested.</p>"""
    total_scheduled_minutes: NotRequired["int"]
    """<p>Total scheduled minutes for an account, specific to the month being requested.</p>"""
    estimated_minutes_remaining: NotRequired["int"]
    """<p>Estimated number of minutes remaining for an account, specific to the month being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMinuteUsageResponse) -> dict:
    out: dict = {}
    if "is_reserved_minutes_customer" in value:
        out["isReservedMinutesCustomer"] = value["is_reserved_minutes_customer"]
    if "total_reserved_minute_allocation" in value:
        out["totalReservedMinuteAllocation"] = value["total_reserved_minute_allocation"]
    if "upcoming_minutes_scheduled" in value:
        out["upcomingMinutesScheduled"] = value["upcoming_minutes_scheduled"]
    if "total_scheduled_minutes" in value:
        out["totalScheduledMinutes"] = value["total_scheduled_minutes"]
    if "estimated_minutes_remaining" in value:
        out["estimatedMinutesRemaining"] = value["estimated_minutes_remaining"]
    return out


def deserialize_json(data: dict) -> GetMinuteUsageResponse:
    out: GetMinuteUsageResponse = {}  # type: ignore[typeddict-item]
    if data.get("isReservedMinutesCustomer") is not None:
        out["is_reserved_minutes_customer"] = data["isReservedMinutesCustomer"]
    if data.get("totalReservedMinuteAllocation") is not None:
        out["total_reserved_minute_allocation"] = data["totalReservedMinuteAllocation"]
    if data.get("upcomingMinutesScheduled") is not None:
        out["upcoming_minutes_scheduled"] = data["upcomingMinutesScheduled"]
    if data.get("totalScheduledMinutes") is not None:
        out["total_scheduled_minutes"] = data["totalScheduledMinutes"]
    if data.get("estimatedMinutesRemaining") is not None:
        out["estimated_minutes_remaining"] = data["estimatedMinutesRemaining"]
    return out
