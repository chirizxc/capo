"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteConnectionOutput``."""

from typing_extensions import NotRequired, TypedDict


class DeleteConnectionOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>The status of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteConnectionOutput:
    out: DeleteConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
