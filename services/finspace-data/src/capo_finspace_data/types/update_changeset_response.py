"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateChangesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.changeset_id
    import capo_finspace_data.types.dataset_id


class UpdateChangesetResponse(TypedDict, closed=True):
    changeset_id: NotRequired["capo_finspace_data.types.changeset_id.ChangesetId"]
    """<p>The unique identifier for the Changeset to update.</p>"""
    dataset_id: NotRequired["capo_finspace_data.types.dataset_id.DatasetId"]
    """<p>The unique identifier for the FinSpace Dataset in which the Changeset is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChangesetResponse) -> dict:
    out: dict = {}
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    return out


def deserialize_json(data: dict) -> UpdateChangesetResponse:
    out: UpdateChangesetResponse = {}  # type: ignore[typeddict-item]
    if data.get("changesetId") is not None:
        out["changeset_id"] = data["changesetId"]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    return out
