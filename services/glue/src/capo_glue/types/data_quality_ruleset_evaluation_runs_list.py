"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetEvaluationRunsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_evaluation_run

DataQualityRulesetEvaluationRunsList: TypeAlias = list[
    "capo_glue.types.data_quality_ruleset_evaluation_run.DataQualityRulesetEvaluationRun"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetEvaluationRunsList) -> list:
    import capo_glue.types.data_quality_ruleset_evaluation_run

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_ruleset_evaluation_run.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityRulesetEvaluationRunsList:
    import capo_glue.types.data_quality_ruleset_evaluation_run

    out: DataQualityRulesetEvaluationRunsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.data_quality_ruleset_evaluation_run.deserialize_aws_json_1_1(
                item
            )
        )
    return out
