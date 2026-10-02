"""Generated from Smithy shape ``com.amazonaws.connect#RuleAttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rule_attribute_and_condition

RuleAttributeOrConditionList: TypeAlias = list[
    "capo_connect.types.rule_attribute_and_condition.RuleAttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleAttributeOrConditionList) -> list:
    import capo_connect.types.rule_attribute_and_condition

    out: list = []
    for item in value:
        out.append(capo_connect.types.rule_attribute_and_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleAttributeOrConditionList:
    import capo_connect.types.rule_attribute_and_condition

    out: RuleAttributeOrConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.rule_attribute_and_condition.deserialize_json(item)
        )
    return out
