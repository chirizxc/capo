"""Generated from Smithy shape ``com.amazonaws.apigateway#PatchOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.op
    import capo_api_gateway.types.string

PatchOperation = TypedDict(
    "PatchOperation",
    {
        "op": NotRequired["capo_api_gateway.types.op.Op"],
        "path": NotRequired["capo_api_gateway.types.string.String"],
        "value": NotRequired["capo_api_gateway.types.string.String"],
        "from": NotRequired["capo_api_gateway.types.string.String"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PatchOperation) -> dict:
    out: dict = {}
    if "op" in value:
        import capo_api_gateway.types.op

        out["op"] = capo_api_gateway.types.op.serialize_json(value["op"])
    if "path" in value:
        out["path"] = value["path"]
    if "value" in value:
        out["value"] = value["value"]
    if "from" in value:
        out["from"] = value["from"]
    return out


def deserialize_json(data: dict) -> PatchOperation:
    out: PatchOperation = {}  # type: ignore[typeddict-item]
    if data.get("op") is not None:
        import capo_api_gateway.types.op

        out["op"] = capo_api_gateway.types.op.deserialize_json(data["op"])
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("from") is not None:
        out["from"] = data["from"]
    return out
