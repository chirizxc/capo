"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PaymentScheduleEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.payment_schedule_entry

PaymentScheduleEntryList: TypeAlias = list[
    "capo_marketplace_discovery.types.payment_schedule_entry.PaymentScheduleEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentScheduleEntryList) -> list:
    import capo_marketplace_discovery.types.payment_schedule_entry

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.payment_schedule_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PaymentScheduleEntryList:
    import capo_marketplace_discovery.types.payment_schedule_entry

    out: PaymentScheduleEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_discovery.types.payment_schedule_entry.deserialize_json(
                item
            )
        )
    return out
