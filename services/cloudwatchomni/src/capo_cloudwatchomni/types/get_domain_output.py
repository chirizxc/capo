"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain


class GetDomainOutput(TypedDict, closed=True):
    domain: "capo_cloudwatchomni.types.domain.Domain"
    """The details of the domain."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDomainOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.domain

    out["domain"] = capo_cloudwatchomni.types.domain.serialize_cbor(value["domain"])
    return out


def deserialize_cbor(data: dict) -> GetDomainOutput:
    out: GetDomainOutput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        import capo_cloudwatchomni.types.domain

        out["domain"] = capo_cloudwatchomni.types.domain.deserialize_cbor(
            data["domain"]
        )
    else:
        raise DeserializationError("GetDomainOutput.domain required")
    return out
