"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportAssetToSignedUrlRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.id


class ExportAssetToSignedUrlRequestDetails(TypedDict, closed=True):
    asset_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the asset that is exported to a signed URL.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this export request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAssetToSignedUrlRequestDetails) -> dict:
    out: dict = {}
    out["AssetId"] = value["asset_id"]
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ExportAssetToSignedUrlRequestDetails:
    out: ExportAssetToSignedUrlRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssetId") is not None:
        out["asset_id"] = data["AssetId"]
    else:
        raise DeserializationError(
            "ExportAssetToSignedUrlRequestDetails.asset_id required"
        )
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ExportAssetToSignedUrlRequestDetails.data_set_id required"
        )
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ExportAssetToSignedUrlRequestDetails.revision_id required"
        )
    return out
