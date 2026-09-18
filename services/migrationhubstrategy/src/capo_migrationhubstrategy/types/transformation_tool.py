"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#TransformationTool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.tranformation_tool_description
    import capo_migrationhubstrategy.types.tranformation_tool_installation_link
    import capo_migrationhubstrategy.types.transformation_tool_name


class TransformationTool(TypedDict, closed=True):
    name: NotRequired[
        "capo_migrationhubstrategy.types.transformation_tool_name.TransformationToolName"
    ]
    """<p> Name of the tool. </p>"""
    description: NotRequired[
        "capo_migrationhubstrategy.types.tranformation_tool_description.TranformationToolDescription"
    ]
    """<p> Description of the tool. </p>"""
    tranformation_tool_installation_link: NotRequired[
        "capo_migrationhubstrategy.types.tranformation_tool_installation_link.TranformationToolInstallationLink"
    ]
    """<p> URL for installing the tool. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformationTool) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tranformation_tool_installation_link" in value:
        out["tranformationToolInstallationLink"] = value[
            "tranformation_tool_installation_link"
        ]
    return out


def deserialize_json(data: dict) -> TransformationTool:
    out: TransformationTool = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tranformationToolInstallationLink") is not None:
        out["tranformation_tool_installation_link"] = data[
            "tranformationToolInstallationLink"
        ]
    return out
