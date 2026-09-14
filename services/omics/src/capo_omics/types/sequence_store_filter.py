"""Generated from Smithy shape ``com.amazonaws.omics#SequenceStoreFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.sequence_store_name
    import capo_omics.types.sequence_store_status


class SequenceStoreFilter(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>A name to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""
    status: NotRequired["capo_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>Filter results based on status.</p>"""
    updated_after: NotRequired["datetime.datetime"]
    """<p>Filter results based on stores updated after the specified time.</p>"""
    updated_before: NotRequired["datetime.datetime"]
    """<p>Filter results based on stores updated before the specified time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequenceStoreFilter) -> dict:
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
    if "status" in value:
        out["status"] = value["status"]
    if "updated_after" in value:
        import capo_omics._protocol.serialize

        out["updatedAfter"] = capo_omics._protocol.serialize.fmt_date_time(
            value["updated_after"]
        )
    if "updated_before" in value:
        import capo_omics._protocol.serialize

        out["updatedBefore"] = capo_omics._protocol.serialize.fmt_date_time(
            value["updated_before"]
        )
    return out


def deserialize_json(data: dict) -> SequenceStoreFilter:
    out: SequenceStoreFilter = {}  # type: ignore[typeddict-item]
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("updatedAfter") is not None:
        import datetime

        out["updated_after"] = datetime.datetime.fromisoformat(
            data["updatedAfter"].replace("Z", "+00:00")
        )
    if data.get("updatedBefore") is not None:
        import datetime

        out["updated_before"] = datetime.datetime.fromisoformat(
            data["updatedBefore"].replace("Z", "+00:00")
        )
    return out
