"""Generated from Smithy shape ``com.amazonaws.support#UploadProgress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.field_integer_value


class UploadProgress(TypedDict, closed=True):
    total_parts: NotRequired["capo_support.types.field_integer_value.FieldIntegerValue"]
    """<p>The total number of parts that the file is split into.</p>"""
    completed_parts_count: NotRequired[
        "capo_support.types.field_integer_value.FieldIntegerValue"
    ]
    """<p>The number of parts that have been successfully uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadProgress) -> dict:
    out: dict = {}
    if "total_parts" in value:
        out["totalParts"] = value["total_parts"]
    if "completed_parts_count" in value:
        out["completedPartsCount"] = value["completed_parts_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadProgress:
    out: UploadProgress = {}  # type: ignore[typeddict-item]
    if data.get("totalParts") is not None:
        out["total_parts"] = data["totalParts"]
    if data.get("completedPartsCount") is not None:
        out["completed_parts_count"] = data["completedPartsCount"]
    return out
