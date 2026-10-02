"""Generated from Smithy shape ``com.amazonaws.glue#IterableFormListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_term_id_list
    import capo_glue.types.item_description
    import capo_glue.types.item_id
    import capo_glue.types.item_name


class IterableFormListItem(TypedDict, closed=True):
    item_id: NotRequired["capo_glue.types.item_id.ItemId"]
    """<p>The unique identifier of the item.</p>"""
    item_name: NotRequired["capo_glue.types.item_name.ItemName"]
    """<p>The name of the item.</p>"""
    description: NotRequired["capo_glue.types.item_description.ItemDescription"]
    """<p>The description of the item.</p>"""
    glossary_terms: NotRequired[
        "capo_glue.types.glossary_term_id_list.GlossaryTermIdList"
    ]
    """<p>The identifiers of the glossary terms associated with the item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IterableFormListItem) -> dict:
    out: dict = {}
    if "item_id" in value:
        out["ItemId"] = value["item_id"]
    if "item_name" in value:
        out["ItemName"] = value["item_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "glossary_terms" in value:
        import capo_glue.types.glossary_term_id_list

        out["GlossaryTerms"] = (
            capo_glue.types.glossary_term_id_list.serialize_aws_json_1_1(
                value["glossary_terms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IterableFormListItem:
    out: IterableFormListItem = {}  # type: ignore[typeddict-item]
    if data.get("ItemId") is not None:
        out["item_id"] = data["ItemId"]
    if data.get("ItemName") is not None:
        out["item_name"] = data["ItemName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("GlossaryTerms") is not None:
        import capo_glue.types.glossary_term_id_list

        out["glossary_terms"] = (
            capo_glue.types.glossary_term_id_list.deserialize_aws_json_1_1(
                data["GlossaryTerms"]
            )
        )
    return out
