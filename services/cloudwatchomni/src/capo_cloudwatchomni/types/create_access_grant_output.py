"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateAccessGrantOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant


class CreateAccessGrantOutput(TypedDict, closed=True):
    access_grant: "capo_cloudwatchomni.types.access_grant.AccessGrant"
    """The details of the created access grant."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAccessGrantOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.access_grant

    out["accessGrant"] = capo_cloudwatchomni.types.access_grant.serialize_cbor(
        value["access_grant"]
    )
    return out


def deserialize_cbor(data: dict) -> CreateAccessGrantOutput:
    out: CreateAccessGrantOutput = {}  # type: ignore[typeddict-item]
    if data.get("accessGrant") is not None:
        import capo_cloudwatchomni.types.access_grant

        out["access_grant"] = capo_cloudwatchomni.types.access_grant.deserialize_cbor(
            data["accessGrant"]
        )
    else:
        raise DeserializationError("CreateAccessGrantOutput.access_grant required")
    return out
