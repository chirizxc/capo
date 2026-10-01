"""Generated from Smithy shape ``com.amazonaws.securityhub#AccountFreeTrialStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.account_free_trial_status

AccountFreeTrialStatusList: TypeAlias = list[
    "capo_securityhub.types.account_free_trial_status.AccountFreeTrialStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountFreeTrialStatusList) -> list:
    import capo_securityhub.types.account_free_trial_status

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.account_free_trial_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccountFreeTrialStatusList:
    import capo_securityhub.types.account_free_trial_status

    out: AccountFreeTrialStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.account_free_trial_status.deserialize_json(item)
        )
    return out
