"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetUploadPartListFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ReadSetUploadPartListFilter(TypedDict, closed=True):
    created_after: NotRequired["datetime.datetime"]
    """<p> Filters for read set uploads after a specified time. </p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p> Filters for read set part uploads before a specified time. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetUploadPartListFilter) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> ReadSetUploadPartListFilter:
    out: ReadSetUploadPartListFilter = {}  # type: ignore[typeddict-item]
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
