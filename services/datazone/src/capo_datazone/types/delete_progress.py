"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteProgress``."""

from typing_extensions import NotRequired, TypedDict


class DeleteProgress(TypedDict, closed=True):
    successfully_deleted_project_count: NotRequired["int"]
    """<p>The number of projects that Amazon DataZone successfully deleted during the domain deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProgress) -> dict:
    out: dict = {}
    if "successfully_deleted_project_count" in value:
        out["successfullyDeletedProjectCount"] = value[
            "successfully_deleted_project_count"
        ]
    return out


def deserialize_json(data: dict) -> DeleteProgress:
    out: DeleteProgress = {}  # type: ignore[typeddict-item]
    if data.get("successfullyDeletedProjectCount") is not None:
        out["successfully_deleted_project_count"] = data[
            "successfullyDeletedProjectCount"
        ]
    return out
