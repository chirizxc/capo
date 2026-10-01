"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.id


class DeleteAssetModelCompositeModelResponse(TypedDict, closed=True):
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    asset_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    if "asset_model_id" in value:
        out["assetModelId"] = value["asset_model_id"]
    return out


def deserialize_json(data: dict) -> DeleteAssetModelCompositeModelResponse:
    out: DeleteAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelStatus") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAssetModelCompositeModelResponse.asset_model_status required"
        )
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    return out
