"""Generated from Smithy shape ``com.amazonaws.glue#GlossaryTermItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_short_description
    import capo_glue.types.glossary_term_id
    import capo_glue.types.glossary_term_name


class GlossaryTermItem(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.glossary_term_id.GlossaryTermId"]
    """<p>The unique identifier of the glossary term.</p>"""
    name: NotRequired["capo_glue.types.glossary_term_name.GlossaryTermName"]
    """<p>The name of the glossary term.</p>"""
    short_description: NotRequired[
        "capo_glue.types.glossary_short_description.GlossaryShortDescription"
    ]
    """<p>The short description of the glossary term.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlossaryTermItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlossaryTermItem:
    out: GlossaryTermItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    return out
