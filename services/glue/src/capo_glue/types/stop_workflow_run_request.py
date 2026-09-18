"""Generated from Smithy shape ``com.amazonaws.glue#StopWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.name_string


class StopWorkflowRunRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the workflow to stop.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the workflow run to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkflowRunRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkflowRunRequest:
    out: StopWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StopWorkflowRunRequest.name required")
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("StopWorkflowRunRequest.run_id required")
    return out
