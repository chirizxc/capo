"""Generated from Smithy shape ``com.amazonaws.glue#SearchAssetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.search_next_token
    import capo_glue.types.search_result_item_list


class SearchAssetsOutput(TypedDict, closed=True):
    items: NotRequired["capo_glue.types.search_result_item_list.SearchResultItemList"]
    """<p>The list of assets matching the search criteria.</p>"""
    next_token: NotRequired["capo_glue.types.search_next_token.SearchNextToken"]
    """<p>A continuation token, present if the current segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchAssetsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_glue.types.search_result_item_list

        out["Items"] = capo_glue.types.search_result_item_list.serialize_aws_json_1_1(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchAssetsOutput:
    out: SearchAssetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_glue.types.search_result_item_list

        out["items"] = capo_glue.types.search_result_item_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
