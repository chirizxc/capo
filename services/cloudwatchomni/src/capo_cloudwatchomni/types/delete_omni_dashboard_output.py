"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteOmniDashboardOutput``."""

from typing_extensions import TypedDict


class DeleteOmniDashboardOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteOmniDashboardOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteOmniDashboardOutput:
    out: DeleteOmniDashboardOutput = {}  # type: ignore[typeddict-item]
    return out
