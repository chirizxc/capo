"""Generated from Smithy shape ``com.amazonaws.devopsagent#ScheduleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.schedule_expression


class ScheduleCondition(TypedDict, closed=True):
    expression: "capo_devops_agent.types.schedule_expression.ScheduleExpression"
    """<p>The schedule expression</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleCondition) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> ScheduleCondition:
    out: ScheduleCondition = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("ScheduleCondition.expression required")
    return out
