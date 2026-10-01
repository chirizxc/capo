"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormAIVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_ai_version_summary

EvaluationFormAIVersionSummaryList: TypeAlias = list[
    "capo_connect.types.evaluation_form_ai_version_summary.EvaluationFormAIVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormAIVersionSummaryList) -> list:
    import capo_connect.types.evaluation_form_ai_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_ai_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormAIVersionSummaryList:
    import capo_connect.types.evaluation_form_ai_version_summary

    out: EvaluationFormAIVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.evaluation_form_ai_version_summary.deserialize_json(item)
        )
    return out
