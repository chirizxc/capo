"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_eventbridgev2.types.tag_map.TagMap"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_eventbridgev2.types.tag_map

        out["Tags"] = capo_eventbridgev2.types.tag_map.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_eventbridgev2.types.tag_map

        out["tags"] = capo_eventbridgev2.types.tag_map.deserialize_cbor(data["Tags"])
    return out
