"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppHolidayScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_holiday_schedule_entry

WhatsAppHolidayScheduleList: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_holiday_schedule_entry.WhatsAppHolidayScheduleEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppHolidayScheduleList) -> list:
    import capo_socialmessaging.types.whats_app_holiday_schedule_entry

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_holiday_schedule_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppHolidayScheduleList:
    import capo_socialmessaging.types.whats_app_holiday_schedule_entry

    out: WhatsAppHolidayScheduleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_socialmessaging.types.whats_app_holiday_schedule_entry.deserialize_json(
                item
            )
        )
    return out
