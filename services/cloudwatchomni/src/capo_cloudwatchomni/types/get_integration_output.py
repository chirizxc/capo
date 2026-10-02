"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration


class GetIntegrationOutput(TypedDict, closed=True):
    integration: "capo_cloudwatchomni.types.integration.Integration"
    """The details of the requested integration."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetIntegrationOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.integration

    out["integration"] = capo_cloudwatchomni.types.integration.serialize_cbor(
        value["integration"]
    )
    return out


def deserialize_cbor(data: dict) -> GetIntegrationOutput:
    out: GetIntegrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("integration") is not None:
        import capo_cloudwatchomni.types.integration

        out["integration"] = capo_cloudwatchomni.types.integration.deserialize_cbor(
            data["integration"]
        )
    else:
        raise DeserializationError("GetIntegrationOutput.integration required")
    return out
