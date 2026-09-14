"""Generated from Smithy shape ``com.amazonaws.athena#QueryStage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.long
    import capo_athena.types.query_stage_plan_node
    import capo_athena.types.query_stages
    import capo_athena.types.string


class QueryStage(TypedDict, closed=True):
    stage_id: NotRequired["capo_athena.types.long.Long"]
    """<p>The identifier for a stage.</p>"""
    state: NotRequired["capo_athena.types.string.String"]
    """<p>State of the stage after query execution.</p>"""
    output_bytes: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of bytes output from the stage after execution.</p>"""
    output_rows: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of rows output from the stage after execution.</p>"""
    input_bytes: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of bytes input into the stage for execution.</p>"""
    input_rows: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of rows input into the stage for execution.</p>"""
    execution_time: NotRequired["capo_athena.types.long.Long"]
    """<p>Time taken to execute this stage.</p>"""
    query_stage_plan: NotRequired[
        "capo_athena.types.query_stage_plan_node.QueryStagePlanNode"
    ]
    """<p>Stage plan information such as name, identifier, sub plans, and source stages.</p>"""
    sub_stages: NotRequired["capo_athena.types.query_stages.QueryStages"]
    """<p>List of sub query stages that form this stage execution plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStage) -> dict:
    out: dict = {}
    if "stage_id" in value:
        out["StageId"] = value["stage_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "output_bytes" in value:
        out["OutputBytes"] = value["output_bytes"]
    if "output_rows" in value:
        out["OutputRows"] = value["output_rows"]
    if "input_bytes" in value:
        out["InputBytes"] = value["input_bytes"]
    if "input_rows" in value:
        out["InputRows"] = value["input_rows"]
    if "execution_time" in value:
        out["ExecutionTime"] = value["execution_time"]
    if "query_stage_plan" in value:
        import capo_athena.types.query_stage_plan_node

        out["QueryStagePlan"] = (
            capo_athena.types.query_stage_plan_node.serialize_aws_json_1_1(
                value["query_stage_plan"]
            )
        )
    if "sub_stages" in value:
        import capo_athena.types.query_stages

        out["SubStages"] = capo_athena.types.query_stages.serialize_aws_json_1_1(
            value["sub_stages"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStage:
    out: QueryStage = {}  # type: ignore[typeddict-item]
    if data.get("StageId") is not None:
        out["stage_id"] = data["StageId"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("OutputBytes") is not None:
        out["output_bytes"] = data["OutputBytes"]
    if data.get("OutputRows") is not None:
        out["output_rows"] = data["OutputRows"]
    if data.get("InputBytes") is not None:
        out["input_bytes"] = data["InputBytes"]
    if data.get("InputRows") is not None:
        out["input_rows"] = data["InputRows"]
    if data.get("ExecutionTime") is not None:
        out["execution_time"] = data["ExecutionTime"]
    if data.get("QueryStagePlan") is not None:
        import capo_athena.types.query_stage_plan_node

        out["query_stage_plan"] = (
            capo_athena.types.query_stage_plan_node.deserialize_aws_json_1_1(
                data["QueryStagePlan"]
            )
        )
    if data.get("SubStages") is not None:
        import capo_athena.types.query_stages

        out["sub_stages"] = capo_athena.types.query_stages.deserialize_aws_json_1_1(
            data["SubStages"]
        )
    return out
