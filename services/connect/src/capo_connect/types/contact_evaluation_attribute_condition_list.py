"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_evaluation_attribute_condition

ContactEvaluationAttributeConditionList: TypeAlias = list[
    "capo_connect.types.contact_evaluation_attribute_condition.ContactEvaluationAttributeCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeConditionList) -> list:
    import capo_connect.types.contact_evaluation_attribute_condition

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.contact_evaluation_attribute_condition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContactEvaluationAttributeConditionList:
    import capo_connect.types.contact_evaluation_attribute_condition

    out: ContactEvaluationAttributeConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.contact_evaluation_attribute_condition.deserialize_json(
                item
            )
        )
    return out
