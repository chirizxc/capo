"""Generated from Smithy shape ``com.amazonaws.glue#StartTriggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class StartTriggerResponse(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the trigger that was started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTriggerResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTriggerResponse:
    out: StartTriggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
