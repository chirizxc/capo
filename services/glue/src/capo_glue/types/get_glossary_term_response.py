"""Generated from Smithy shape ``com.amazonaws.glue#GetGlossaryTermResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_id
    import capo_glue.types.glossary_long_description
    import capo_glue.types.glossary_short_description
    import capo_glue.types.glossary_term_id
    import capo_glue.types.glossary_term_name


class GetGlossaryTermResponse(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.glossary_term_id.GlossaryTermId"]
    """<p>The unique identifier of the glossary term.</p>"""
    glossary_id: NotRequired["capo_glue.types.glossary_id.GlossaryId"]
    """<p>The unique identifier of the glossary containing this term.</p>"""
    name: NotRequired["capo_glue.types.glossary_term_name.GlossaryTermName"]
    """<p>The name of the glossary term.</p>"""
    short_description: NotRequired[
        "capo_glue.types.glossary_short_description.GlossaryShortDescription"
    ]
    """<p>The short description of the glossary term.</p>"""
    long_description: NotRequired[
        "capo_glue.types.glossary_long_description.GlossaryLongDescription"
    ]
    """<p>The long description of the glossary term.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGlossaryTermResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "glossary_id" in value:
        out["GlossaryId"] = value["glossary_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGlossaryTermResponse:
    out: GetGlossaryTermResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("GlossaryId") is not None:
        out["glossary_id"] = data["GlossaryId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    if data.get("LongDescription") is not None:
        out["long_description"] = data["LongDescription"]
    return out
