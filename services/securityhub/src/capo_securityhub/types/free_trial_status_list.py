"""Generated from Smithy shape ``com.amazonaws.securityhub#FreeTrialStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.free_trial_status

FreeTrialStatusList: TypeAlias = list[
    "capo_securityhub.types.free_trial_status.FreeTrialStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialStatusList) -> list:
    import capo_securityhub.types.free_trial_status

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.free_trial_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeTrialStatusList:
    import capo_securityhub.types.free_trial_status

    out: FreeTrialStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.free_trial_status.deserialize_json(item))
    return out
