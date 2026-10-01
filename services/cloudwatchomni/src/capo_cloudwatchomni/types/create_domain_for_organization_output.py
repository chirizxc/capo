"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateDomainForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.organization_domain


class CreateDomainForOrganizationOutput(TypedDict, closed=True):
    organization_domain: (
        "capo_cloudwatchomni.types.organization_domain.OrganizationDomain"
    )
    """The details of the created organization domain."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateDomainForOrganizationOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.organization_domain

    out["organizationDomain"] = (
        capo_cloudwatchomni.types.organization_domain.serialize_cbor(
            value["organization_domain"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> CreateDomainForOrganizationOutput:
    out: CreateDomainForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("organizationDomain") is not None:
        import capo_cloudwatchomni.types.organization_domain

        out["organization_domain"] = (
            capo_cloudwatchomni.types.organization_domain.deserialize_cbor(
                data["organizationDomain"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDomainForOrganizationOutput.organization_domain required"
        )
    return out
