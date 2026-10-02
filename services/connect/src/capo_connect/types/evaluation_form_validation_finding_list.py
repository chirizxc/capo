"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormValidationFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_validation_finding

EvaluationFormValidationFindingList: TypeAlias = list[
    "capo_connect.types.evaluation_form_validation_finding.EvaluationFormValidationFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormValidationFindingList) -> list:
    import capo_connect.types.evaluation_form_validation_finding

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_validation_finding.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormValidationFindingList:
    import capo_connect.types.evaluation_form_validation_finding

    out: EvaluationFormValidationFindingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.evaluation_form_validation_finding.deserialize_json(item)
        )
    return out
