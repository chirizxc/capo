"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityRulesetEvaluationRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_evaluation_run_id_list
    import capo_glue.types.data_quality_ruleset_evaluation_runs_list


class BatchGetDataQualityRulesetEvaluationRunResponse(TypedDict, closed=True):
    runs: NotRequired[
        "capo_glue.types.data_quality_ruleset_evaluation_runs_list.DataQualityRulesetEvaluationRunsList"
    ]
    """<p>A list of evaluation run details for the requested run IDs.</p>"""
    runs_not_found: NotRequired[
        "capo_glue.types.data_quality_ruleset_evaluation_run_id_list.DataQualityRulesetEvaluationRunIdList"
    ]
    """<p>A list of run IDs that were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchGetDataQualityRulesetEvaluationRunResponse,
) -> dict:
    out: dict = {}
    if "runs" in value:
        import capo_glue.types.data_quality_ruleset_evaluation_runs_list

        out["Runs"] = (
            capo_glue.types.data_quality_ruleset_evaluation_runs_list.serialize_aws_json_1_1(
                value["runs"]
            )
        )
    if "runs_not_found" in value:
        import capo_glue.types.data_quality_ruleset_evaluation_run_id_list

        out["RunsNotFound"] = (
            capo_glue.types.data_quality_ruleset_evaluation_run_id_list.serialize_aws_json_1_1(
                value["runs_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchGetDataQualityRulesetEvaluationRunResponse:
    out: BatchGetDataQualityRulesetEvaluationRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("Runs") is not None:
        import capo_glue.types.data_quality_ruleset_evaluation_runs_list

        out["runs"] = (
            capo_glue.types.data_quality_ruleset_evaluation_runs_list.deserialize_aws_json_1_1(
                data["Runs"]
            )
        )
    if data.get("RunsNotFound") is not None:
        import capo_glue.types.data_quality_ruleset_evaluation_run_id_list

        out["runs_not_found"] = (
            capo_glue.types.data_quality_ruleset_evaluation_run_id_list.deserialize_aws_json_1_1(
                data["RunsNotFound"]
            )
        )
    return out
