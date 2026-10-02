"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.account_id

DetectionRuleAccountIds: TypeAlias = list["capo_guardduty.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleAccountIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DetectionRuleAccountIds:
    return [item for item in data if item is not None]
