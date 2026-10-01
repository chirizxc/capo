"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateDomainForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.organization_domain


class UpdateDomainForOrganizationOutput(TypedDict, closed=True):
    organization_domain: (
        "capo_cloudwatchomni.types.organization_domain.OrganizationDomain"
    )
    """The details of the updated organization domain."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateDomainForOrganizationOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.organization_domain

    out["organizationDomain"] = (
        capo_cloudwatchomni.types.organization_domain.serialize_cbor(
            value["organization_domain"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> UpdateDomainForOrganizationOutput:
    out: UpdateDomainForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("organizationDomain") is not None:
        import capo_cloudwatchomni.types.organization_domain

        out["organization_domain"] = (
            capo_cloudwatchomni.types.organization_domain.deserialize_cbor(
                data["organizationDomain"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDomainForOrganizationOutput.organization_domain required"
        )
    return out
