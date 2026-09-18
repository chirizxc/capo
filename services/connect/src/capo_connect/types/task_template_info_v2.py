"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateInfoV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.task_template_name


class TaskTemplateInfoV2(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the task template used to create this contact.</p>"""
    name: NotRequired["capo_connect.types.task_template_name.TaskTemplateName"]
    """<p>The name of the task template used to create this contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateInfoV2) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TaskTemplateInfoV2:
    out: TaskTemplateInfoV2 = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
