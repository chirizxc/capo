"""Generated from Smithy shape ``com.amazonaws.securityhub#FreeTrialAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.free_trial_account_id

FreeTrialAccountIdList: TypeAlias = list[
    "capo_securityhub.types.free_trial_account_id.FreeTrialAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> FreeTrialAccountIdList:
    return [item for item in data if item is not None]
