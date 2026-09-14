"""Generated from Smithy shape ``com.amazonaws.rekognition#Parent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.string


class Parent(TypedDict, closed=True):
    name: NotRequired["capo_rekognition.types.string.String"]
    """<p>The name of the parent label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parent) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Parent:
    out: Parent = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
