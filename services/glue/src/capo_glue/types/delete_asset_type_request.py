"""Generated from Smithy shape ``com.amazonaws.glue#DeleteAssetTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.asset_type_id


class DeleteAssetTypeRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.asset_type_id.AssetTypeId"
    """<p>The identifier of the asset type to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssetTypeRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssetTypeRequest:
    out: DeleteAssetTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("DeleteAssetTypeRequest.identifier required")
    return out
