"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.intermediate_table_arn
    import capo_cleanrooms.types.uuid


class IntermediateTableOutputConfiguration(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the intermediate table.</p>"""
    arn: "capo_cleanrooms.types.intermediate_table_arn.IntermediateTableArn"
    """<p>The Amazon Resource Name (ARN) of the intermediate table.</p>"""
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableOutputConfiguration) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IntermediateTableOutputConfiguration:
    out: IntermediateTableOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("IntermediateTableOutputConfiguration.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IntermediateTableOutputConfiguration.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IntermediateTableOutputConfiguration.name required")
    return out
