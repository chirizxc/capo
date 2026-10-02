"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateSpaceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.space


class CreateSpaceOutput(TypedDict, closed=True):
    space: "capo_cloudwatchomni.types.space.Space"
    """The details of the created space."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSpaceOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.space

    out["space"] = capo_cloudwatchomni.types.space.serialize_cbor(value["space"])
    return out


def deserialize_cbor(data: dict) -> CreateSpaceOutput:
    out: CreateSpaceOutput = {}  # type: ignore[typeddict-item]
    if data.get("space") is not None:
        import capo_cloudwatchomni.types.space

        out["space"] = capo_cloudwatchomni.types.space.deserialize_cbor(data["space"])
    else:
        raise DeserializationError("CreateSpaceOutput.space required")
    return out
