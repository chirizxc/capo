"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoreThresholdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_score_threshold

EvaluationFormScoreThresholdList: TypeAlias = list[
    "capo_connect.types.evaluation_form_score_threshold.EvaluationFormScoreThreshold"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormScoreThresholdList) -> list:
    import capo_connect.types.evaluation_form_score_threshold

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_score_threshold.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormScoreThresholdList:
    import capo_connect.types.evaluation_form_score_threshold

    out: EvaluationFormScoreThresholdList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.evaluation_form_score_threshold.deserialize_json(item)
        )
    return out
