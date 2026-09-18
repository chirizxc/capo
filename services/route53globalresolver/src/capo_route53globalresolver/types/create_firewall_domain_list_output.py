"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateFirewallDomainListOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class CreateFirewallDomainListOutput(TypedDict, closed=True):
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>An Amazon Resource Name (ARN) for the domain list.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver that the domain list is associated with.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the domain list was created on.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>Description for the domain list.</p>"""
    domain_count: "int"
    """<p>Number of domains in the domain list.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the domain list.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the domain list.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>Creation status of the domain list.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the domain list was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFirewallDomainListOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["globalResolverId"] = value["global_resolver_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["domainCount"] = value["domain_count"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateFirewallDomainListOutput:
    out: CreateFirewallDomainListOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateFirewallDomainListOutput.arn required")
    if data.get("globalResolverId") is not None:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError(
            "CreateFirewallDomainListOutput.global_resolver_id required"
        )
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateFirewallDomainListOutput.created_at required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("domainCount") is not None:
        out["domain_count"] = data["domainCount"]
    else:
        raise DeserializationError(
            "CreateFirewallDomainListOutput.domain_count required"
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateFirewallDomainListOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFirewallDomainListOutput.name required")
    if data.get("status") is not None:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateFirewallDomainListOutput.status required")
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateFirewallDomainListOutput.updated_at required")
    return out
