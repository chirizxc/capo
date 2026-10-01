"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListDomainAccessGrantsForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.next_token
    import capo_cloudwatchomni.types.organization_grant_permission
    import capo_cloudwatchomni.types.organization_grant_principal_type
    import capo_cloudwatchomni.types.principal_id


class ListDomainAccessGrantsForOrganizationInput(TypedDict, closed=True):
    domain_id: NotRequired["capo_cloudwatchomni.types.domain_id.DomainId"]
    """Filter by domain ID."""
    principal_id: NotRequired["capo_cloudwatchomni.types.principal_id.PrincipalId"]
    """Filter by principal ID."""
    principal_type: NotRequired[
        "capo_cloudwatchomni.types.organization_grant_principal_type.OrganizationGrantPrincipalType"
    ]
    """Filter by principal type."""
    permission: NotRequired[
        "capo_cloudwatchomni.types.organization_grant_permission.OrganizationGrantPermission"
    ]
    """Filter by permission level."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours."""
    max_results: NotRequired["int"]
    """The maximum number of access grants to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDomainAccessGrantsForOrganizationInput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "principal_type" in value:
        import capo_cloudwatchomni.types.organization_grant_principal_type

        out["principalType"] = (
            capo_cloudwatchomni.types.organization_grant_principal_type.serialize_cbor(
                value["principal_type"]
            )
        )
    if "permission" in value:
        import capo_cloudwatchomni.types.organization_grant_permission

        out["permission"] = (
            capo_cloudwatchomni.types.organization_grant_permission.serialize_cbor(
                value["permission"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListDomainAccessGrantsForOrganizationInput:
    out: ListDomainAccessGrantsForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("principalType") is not None:
        import capo_cloudwatchomni.types.organization_grant_principal_type

        out["principal_type"] = (
            capo_cloudwatchomni.types.organization_grant_principal_type.deserialize_cbor(
                data["principalType"]
            )
        )
    if data.get("permission") is not None:
        import capo_cloudwatchomni.types.organization_grant_permission

        out["permission"] = (
            capo_cloudwatchomni.types.organization_grant_permission.deserialize_cbor(
                data["permission"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
