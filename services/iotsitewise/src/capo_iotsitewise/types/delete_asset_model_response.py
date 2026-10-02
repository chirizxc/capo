"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.id


class DeleteAssetModelResponse(TypedDict, closed=True):
    asset_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset model.</p>"""
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The status of the asset model, which contains a state (<code>DELETING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelResponse) -> dict:
    out: dict = {}
    if "asset_model_id" in value:
        out["assetModelId"] = value["asset_model_id"]
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAssetModelResponse:
    out: DeleteAssetModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    if data.get("assetModelStatus") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAssetModelResponse.asset_model_status required"
        )
    return out
