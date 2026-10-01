"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetEnrichment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_enrichment_entry


class DatasetEnrichment(TypedDict, closed=True):
    video: NotRequired[
        "capo_iotsitewise.types.dataset_enrichment_entry.DatasetEnrichmentEntry"
    ]
    """<p>The enrichment status for video data in the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetEnrichment) -> dict:
    out: dict = {}
    if "video" in value:
        import capo_iotsitewise.types.dataset_enrichment_entry

        out["video"] = capo_iotsitewise.types.dataset_enrichment_entry.serialize_json(
            value["video"]
        )
    return out


def deserialize_json(data: dict) -> DatasetEnrichment:
    out: DatasetEnrichment = {}  # type: ignore[typeddict-item]
    if data.get("video") is not None:
        import capo_iotsitewise.types.dataset_enrichment_entry

        out["video"] = capo_iotsitewise.types.dataset_enrichment_entry.deserialize_json(
            data["video"]
        )
    return out
