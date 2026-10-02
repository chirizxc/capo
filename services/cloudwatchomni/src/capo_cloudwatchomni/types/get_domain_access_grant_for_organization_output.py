"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetDomainAccessGrantForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.organization_access_grant


class GetDomainAccessGrantForOrganizationOutput(TypedDict, closed=True):
    access_grant: (
        "capo_cloudwatchomni.types.organization_access_grant.OrganizationAccessGrant"
    )
    """The retrieved organization access grant."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDomainAccessGrantForOrganizationOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.organization_access_grant

    out["accessGrant"] = (
        capo_cloudwatchomni.types.organization_access_grant.serialize_cbor(
            value["access_grant"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> GetDomainAccessGrantForOrganizationOutput:
    out: GetDomainAccessGrantForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("accessGrant") is not None:
        import capo_cloudwatchomni.types.organization_access_grant

        out["access_grant"] = (
            capo_cloudwatchomni.types.organization_access_grant.deserialize_cbor(
                data["accessGrant"]
            )
        )
    else:
        raise DeserializationError(
            "GetDomainAccessGrantForOrganizationOutput.access_grant required"
        )
    return out
