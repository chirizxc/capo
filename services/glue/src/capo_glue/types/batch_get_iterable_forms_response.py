"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetIterableFormsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.item_error_list
    import capo_glue.types.iterable_form_item_list


class BatchGetIterableFormsResponse(TypedDict, closed=True):
    items: NotRequired["capo_glue.types.iterable_form_item_list.IterableFormItemList"]
    """<p>The list of retrieved iterable form items.</p>"""
    errors: NotRequired["capo_glue.types.item_error_list.ItemErrorList"]
    """<p>The list of errors for items that could not be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetIterableFormsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_glue.types.iterable_form_item_list

        out["Items"] = capo_glue.types.iterable_form_item_list.serialize_aws_json_1_1(
            value["items"]
        )
    if "errors" in value:
        import capo_glue.types.item_error_list

        out["Errors"] = capo_glue.types.item_error_list.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetIterableFormsResponse:
    out: BatchGetIterableFormsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_glue.types.iterable_form_item_list

        out["items"] = capo_glue.types.iterable_form_item_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    if data.get("Errors") is not None:
        import capo_glue.types.item_error_list

        out["errors"] = capo_glue.types.item_error_list.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
