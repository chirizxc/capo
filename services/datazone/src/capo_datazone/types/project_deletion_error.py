"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectDeletionError``."""

from typing_extensions import NotRequired, TypedDict


class ProjectDeletionError(TypedDict, closed=True):
    code: NotRequired["str"]
    """<p>The code of the project deletion error.</p>"""
    message: NotRequired["str"]
    """<p>The message of the project deletion error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectDeletionError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ProjectDeletionError:
    out: ProjectDeletionError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
