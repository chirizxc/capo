"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_partnercentral_revenue_measurement.types.tag_list.TagList"]
    """<p>The tags associated with the resource.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_partnercentral_revenue_measurement.types.tag_list

        out["tags"] = (
            capo_partnercentral_revenue_measurement.types.tag_list.serialize_cbor(
                value["tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_partnercentral_revenue_measurement.types.tag_list

        out["tags"] = (
            capo_partnercentral_revenue_measurement.types.tag_list.deserialize_cbor(
                data["tags"]
            )
        )
    return out
