"""Generated from Smithy shape ``com.amazonaws.billingconductor#PrimaryAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id

PrimaryAccountIdList: TypeAlias = list[
    "capo_billingconductor.types.account_id.AccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrimaryAccountIdList:
    return [item for item in data if item is not None]
