"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateBacklogTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.task


class CreateBacklogTaskResponse(TypedDict, closed=True):
    task: "capo_devops_agent.types.task.Task"
    """<p>The newly created task object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBacklogTaskResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.task

    out["task"] = capo_devops_agent.types.task.serialize_json(value["task"])
    return out


def deserialize_json(data: dict) -> CreateBacklogTaskResponse:
    out: CreateBacklogTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("task") is not None:
        import capo_devops_agent.types.task

        out["task"] = capo_devops_agent.types.task.deserialize_json(data["task"])
    else:
        raise DeserializationError("CreateBacklogTaskResponse.task required")
    return out
