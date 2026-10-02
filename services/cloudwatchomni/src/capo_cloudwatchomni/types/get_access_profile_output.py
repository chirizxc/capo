"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetAccessProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_profile


class GetAccessProfileOutput(TypedDict, closed=True):
    access_profile: "capo_cloudwatchomni.types.access_profile.AccessProfile"
    """The access profile."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAccessProfileOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.access_profile

    out["accessProfile"] = capo_cloudwatchomni.types.access_profile.serialize_cbor(
        value["access_profile"]
    )
    return out


def deserialize_cbor(data: dict) -> GetAccessProfileOutput:
    out: GetAccessProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("accessProfile") is not None:
        import capo_cloudwatchomni.types.access_profile

        out["access_profile"] = (
            capo_cloudwatchomni.types.access_profile.deserialize_cbor(
                data["accessProfile"]
            )
        )
    else:
        raise DeserializationError("GetAccessProfileOutput.access_profile required")
    return out
