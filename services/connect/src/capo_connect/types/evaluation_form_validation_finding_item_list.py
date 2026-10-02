"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormValidationFindingItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_validation_finding_item

EvaluationFormValidationFindingItemList: TypeAlias = list[
    "capo_connect.types.evaluation_form_validation_finding_item.EvaluationFormValidationFindingItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormValidationFindingItemList) -> list:
    import capo_connect.types.evaluation_form_validation_finding_item

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_validation_finding_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormValidationFindingItemList:
    import capo_connect.types.evaluation_form_validation_finding_item

    out: EvaluationFormValidationFindingItemList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.evaluation_form_validation_finding_item.deserialize_json(
                item
            )
        )
    return out
