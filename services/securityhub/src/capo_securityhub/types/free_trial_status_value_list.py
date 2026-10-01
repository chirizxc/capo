"""Generated from Smithy shape ``com.amazonaws.securityhub#FreeTrialStatusValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.free_trial_status_value

FreeTrialStatusValueList: TypeAlias = list[
    "capo_securityhub.types.free_trial_status_value.FreeTrialStatusValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialStatusValueList) -> list:
    import capo_securityhub.types.free_trial_status_value

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.free_trial_status_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeTrialStatusValueList:
    import capo_securityhub.types.free_trial_status_value

    out: FreeTrialStatusValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.free_trial_status_value.deserialize_json(item)
        )
    return out
