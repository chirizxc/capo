"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateAccessProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_profile


class CreateAccessProfileOutput(TypedDict, closed=True):
    access_profile: "capo_cloudwatchomni.types.access_profile.AccessProfile"
    """The access profile."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAccessProfileOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.access_profile

    out["accessProfile"] = capo_cloudwatchomni.types.access_profile.serialize_cbor(
        value["access_profile"]
    )
    return out


def deserialize_cbor(data: dict) -> CreateAccessProfileOutput:
    out: CreateAccessProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("accessProfile") is not None:
        import capo_cloudwatchomni.types.access_profile

        out["access_profile"] = (
            capo_cloudwatchomni.types.access_profile.deserialize_cbor(
                data["accessProfile"]
            )
        )
    else:
        raise DeserializationError("CreateAccessProfileOutput.access_profile required")
    return out
