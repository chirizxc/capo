"""Generated from Smithy shape ``com.amazonaws.datazone#FailureCause``."""

from typing_extensions import NotRequired, TypedDict


class FailureCause(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>The description of the error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureCause) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FailureCause:
    out: FailureCause = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
