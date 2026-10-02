"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetAccessGrantOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant


class GetAccessGrantOutput(TypedDict, closed=True):
    access_grant: "capo_cloudwatchomni.types.access_grant.AccessGrant"
    """The full details of the access grant."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAccessGrantOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.access_grant

    out["accessGrant"] = capo_cloudwatchomni.types.access_grant.serialize_cbor(
        value["access_grant"]
    )
    return out


def deserialize_cbor(data: dict) -> GetAccessGrantOutput:
    out: GetAccessGrantOutput = {}  # type: ignore[typeddict-item]
    if data.get("accessGrant") is not None:
        import capo_cloudwatchomni.types.access_grant

        out["access_grant"] = capo_cloudwatchomni.types.access_grant.deserialize_cbor(
            data["accessGrant"]
        )
    else:
        raise DeserializationError("GetAccessGrantOutput.access_grant required")
    return out
