"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_map
    import capo_dynamodb.types.score_number


class SearchResultItem(TypedDict, closed=True):
    item: NotRequired["capo_dynamodb.types.attribute_map.AttributeMap"]
    """<p>A map of attribute names to <code>AttributeValue</code> objects, representing the projected attributes of the item returned by the vector search.</p>"""
    score: "capo_dynamodb.types.score_number.ScoreNumber"
    """<p>The similarity score for this item relative to the search vector. The interpretation depends on the distance function configured for the vector index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchResultItem) -> dict:
    out: dict = {}
    if "item" in value:
        import capo_dynamodb.types.attribute_map

        out["Item"] = capo_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    out["Score"] = (
        "NaN"
        if value.get("score", 0) != value.get("score", 0)
        else "Infinity"
        if value.get("score", 0) == float("inf")
        else "-Infinity"
        if value.get("score", 0) == float("-inf")
        else value.get("score", 0)
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchResultItem:
    out: SearchResultItem = {}  # type: ignore[typeddict-item]
    if data.get("Item") is not None:
        import capo_dynamodb.types.attribute_map

        out["item"] = capo_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    else:
        out["score"] = 0
    return out
