"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppWeeklyOperatingHoursList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_weekly_operating_hours_entry

WhatsAppWeeklyOperatingHoursList: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_weekly_operating_hours_entry.WhatsAppWeeklyOperatingHoursEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppWeeklyOperatingHoursList) -> list:
    import capo_socialmessaging.types.whats_app_weekly_operating_hours_entry

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_weekly_operating_hours_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppWeeklyOperatingHoursList:
    import capo_socialmessaging.types.whats_app_weekly_operating_hours_entry

    out: WhatsAppWeeklyOperatingHoursList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_socialmessaging.types.whats_app_weekly_operating_hours_entry.deserialize_json(
                item
            )
        )
    return out
