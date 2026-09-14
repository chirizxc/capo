"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceStoreFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.reference_store_name


class ReferenceStoreFilter(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.reference_store_name.ReferenceStoreName"]
    """<p>The name to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceStoreFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "created_after" in value:
        import capo_omics._protocol.serialize

        out["createdAfter"] = capo_omics._protocol.serialize.fmt_date_time(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_omics._protocol.serialize

        out["createdBefore"] = capo_omics._protocol.serialize.fmt_date_time(
            value["created_before"]
        )
    return out


def deserialize_json(data: dict) -> ReferenceStoreFilter:
    out: ReferenceStoreFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("createdAfter") is not None:
        import datetime

        out["created_after"] = datetime.datetime.fromisoformat(
            data["createdAfter"].replace("Z", "+00:00")
        )
    if data.get("createdBefore") is not None:
        import datetime

        out["created_before"] = datetime.datetime.fromisoformat(
            data["createdBefore"].replace("Z", "+00:00")
        )
    return out
