"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetIntelligenceConfigurationInput``."""

from typing_extensions import TypedDict


class GetIntelligenceConfigurationInput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetIntelligenceConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetIntelligenceConfigurationInput:
    out: GetIntelligenceConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
