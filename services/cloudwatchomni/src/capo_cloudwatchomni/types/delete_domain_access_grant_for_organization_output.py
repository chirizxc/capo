"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteDomainAccessGrantForOrganizationOutput``."""

from typing_extensions import TypedDict


class DeleteDomainAccessGrantForOrganizationOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDomainAccessGrantForOrganizationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteDomainAccessGrantForOrganizationOutput:
    out: DeleteDomainAccessGrantForOrganizationOutput = {}  # type: ignore[typeddict-item]
    return out
