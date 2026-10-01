"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteDomainForOrganizationOutput``."""

from typing_extensions import TypedDict


class DeleteDomainForOrganizationOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDomainForOrganizationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteDomainForOrganizationOutput:
    out: DeleteDomainForOrganizationOutput = {}  # type: ignore[typeddict-item]
    return out
