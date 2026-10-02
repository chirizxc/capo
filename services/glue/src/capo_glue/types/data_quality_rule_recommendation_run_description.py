"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleRecommendationRunDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.recommendation_mode
    import capo_glue.types.task_status_type
    import capo_glue.types.timestamp


class DataQualityRuleRecommendationRunDescription(TypedDict, closed=True):
    run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""
    status: NotRequired["capo_glue.types.task_status_type.TaskStatusType"]
    """<p>The status for this run.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this run started.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The data source (Glue table) associated with the recommendation run.</p>"""
    created_ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the ruleset that was created by the recommendation run.</p>"""
    recommendation_mode: NotRequired[
        "capo_glue.types.recommendation_mode.RecommendationMode"
    ]
    """<p>The mode that Glue Data Quality uses to recommend rules.</p> <p>The default is <code>BASIC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleRecommendationRunDescription) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "status" in value:
        import capo_glue.types.task_status_type

        out["Status"] = capo_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "started_on" in value:
        import capo_glue.types.timestamp

        out["StartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "created_ruleset_name" in value:
        out["CreatedRulesetName"] = value["created_ruleset_name"]
    if "recommendation_mode" in value:
        import capo_glue.types.recommendation_mode

        out["RecommendationMode"] = (
            capo_glue.types.recommendation_mode.serialize_aws_json_1_1(
                value["recommendation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRuleRecommendationRunDescription:
    out: DataQualityRuleRecommendationRunDescription = {}  # type: ignore[typeddict-item]
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    if data.get("Status") is not None:
        import capo_glue.types.task_status_type

        out["status"] = capo_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StartedOn") is not None:
        import capo_glue.types.timestamp

        out["started_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("CreatedRulesetName") is not None:
        out["created_ruleset_name"] = data["CreatedRulesetName"]
    if data.get("RecommendationMode") is not None:
        import capo_glue.types.recommendation_mode

        out["recommendation_mode"] = (
            capo_glue.types.recommendation_mode.deserialize_aws_json_1_1(
                data["RecommendationMode"]
            )
        )
    return out
