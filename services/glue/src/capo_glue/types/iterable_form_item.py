"""Generated from Smithy shape ``com.amazonaws.glue#IterableFormItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_form_map
    import capo_glue.types.glossary_term_id_list
    import capo_glue.types.item_id
    import capo_glue.types.item_name


class IterableFormItem(TypedDict, closed=True):
    item_id: NotRequired["capo_glue.types.item_id.ItemId"]
    """<p>The unique identifier of the item.</p>"""
    item_name: NotRequired["capo_glue.types.item_name.ItemName"]
    """<p>The name of the item.</p>"""
    glossary_terms: NotRequired[
        "capo_glue.types.glossary_term_id_list.GlossaryTermIdList"
    ]
    """<p>The identifiers of the glossary terms associated with the item.</p>"""
    forms: NotRequired["capo_glue.types.asset_form_map.AssetFormMap"]
    """<p>The forms on the item, keyed by form name.</p>"""
    attachments: NotRequired["capo_glue.types.asset_form_map.AssetFormMap"]
    """<p>Additional attachments on the item for more context, keyed by attachment name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IterableFormItem) -> dict:
    out: dict = {}
    if "item_id" in value:
        out["ItemId"] = value["item_id"]
    if "item_name" in value:
        out["ItemName"] = value["item_name"]
    if "glossary_terms" in value:
        import capo_glue.types.glossary_term_id_list

        out["GlossaryTerms"] = (
            capo_glue.types.glossary_term_id_list.serialize_aws_json_1_1(
                value["glossary_terms"]
            )
        )
    if "forms" in value:
        import capo_glue.types.asset_form_map

        out["Forms"] = capo_glue.types.asset_form_map.serialize_aws_json_1_1(
            value["forms"]
        )
    if "attachments" in value:
        import capo_glue.types.asset_form_map

        out["Attachments"] = capo_glue.types.asset_form_map.serialize_aws_json_1_1(
            value["attachments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IterableFormItem:
    out: IterableFormItem = {}  # type: ignore[typeddict-item]
    if data.get("ItemId") is not None:
        out["item_id"] = data["ItemId"]
    if data.get("ItemName") is not None:
        out["item_name"] = data["ItemName"]
    if data.get("GlossaryTerms") is not None:
        import capo_glue.types.glossary_term_id_list

        out["glossary_terms"] = (
            capo_glue.types.glossary_term_id_list.deserialize_aws_json_1_1(
                data["GlossaryTerms"]
            )
        )
    if data.get("Forms") is not None:
        import capo_glue.types.asset_form_map

        out["forms"] = capo_glue.types.asset_form_map.deserialize_aws_json_1_1(
            data["Forms"]
        )
    if data.get("Attachments") is not None:
        import capo_glue.types.asset_form_map

        out["attachments"] = capo_glue.types.asset_form_map.deserialize_aws_json_1_1(
            data["Attachments"]
        )
    return out
