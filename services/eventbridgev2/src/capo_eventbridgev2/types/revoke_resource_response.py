"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#RevokeResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.revocable_resource_arn


class RevokeResourceResponse(TypedDict, closed=True):
    arn: NotRequired[
        "capo_eventbridgev2.types.revocable_resource_arn.RevocableResourceArn"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevokeResourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> RevokeResourceResponse:
    out: RevokeResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
