"""Generated from Smithy shape ``com.amazonaws.glue#Statement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.double_value
    import capo_glue.types.generic_string
    import capo_glue.types.integer_value
    import capo_glue.types.long_value
    import capo_glue.types.statement_output
    import capo_glue.types.statement_state


class Statement(TypedDict, closed=True):
    id: "capo_glue.types.integer_value.IntegerValue"
    """<p>The ID of the statement.</p>"""
    code: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The execution code of the statement.</p>"""
    state: NotRequired["capo_glue.types.statement_state.StatementState"]
    """<p>The state while request is actioned.</p>"""
    output: NotRequired["capo_glue.types.statement_output.StatementOutput"]
    """<p>The output in JSON.</p>"""
    progress: "capo_glue.types.double_value.DoubleValue"
    """<p>The code execution progress.</p>"""
    started_on: "capo_glue.types.long_value.LongValue"
    """<p>The unix time and date that the job definition was started.</p>"""
    completed_on: "capo_glue.types.long_value.LongValue"
    """<p>The unix time and date that the job definition was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statement) -> dict:
    out: dict = {}
    out["Id"] = value.get("id", 0)
    if "code" in value:
        out["Code"] = value["code"]
    if "state" in value:
        import capo_glue.types.statement_state

        out["State"] = capo_glue.types.statement_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "output" in value:
        import capo_glue.types.statement_output

        out["Output"] = capo_glue.types.statement_output.serialize_aws_json_1_1(
            value["output"]
        )
    out["Progress"] = (
        "NaN"
        if value.get("progress", 0) != value.get("progress", 0)
        else "Infinity"
        if value.get("progress", 0) == float("inf")
        else "-Infinity"
        if value.get("progress", 0) == float("-inf")
        else value.get("progress", 0)
    )
    out["StartedOn"] = value.get("started_on", 0)
    out["CompletedOn"] = value.get("completed_on", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Statement:
    out: Statement = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = 0
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("State") is not None:
        import capo_glue.types.statement_state

        out["state"] = capo_glue.types.statement_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Output") is not None:
        import capo_glue.types.statement_output

        out["output"] = capo_glue.types.statement_output.deserialize_aws_json_1_1(
            data["Output"]
        )
    if data.get("Progress") is not None:
        out["progress"] = float(data["Progress"])
    else:
        out["progress"] = 0
    if data.get("StartedOn") is not None:
        out["started_on"] = data["StartedOn"]
    else:
        out["started_on"] = 0
    if data.get("CompletedOn") is not None:
        out["completed_on"] = data["CompletedOn"]
    else:
        out["completed_on"] = 0
    return out
