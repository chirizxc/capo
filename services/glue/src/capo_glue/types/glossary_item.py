"""Generated from Smithy shape ``com.amazonaws.glue#GlossaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_id
    import capo_glue.types.glossary_name
    import capo_glue.types.metadata_description


class GlossaryItem(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.glossary_id.GlossaryId"]
    """<p>The unique identifier of the glossary.</p>"""
    name: NotRequired["capo_glue.types.glossary_name.GlossaryName"]
    """<p>The name of the glossary.</p>"""
    description: NotRequired["capo_glue.types.metadata_description.MetadataDescription"]
    """<p>The description of the glossary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlossaryItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlossaryItem:
    out: GlossaryItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
