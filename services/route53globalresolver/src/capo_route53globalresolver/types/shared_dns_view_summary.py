"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#SharedDNSViewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.account_id
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.dns_sec_validation_type
    import capo_route53globalresolver.types.edns_client_subnet_type
    import capo_route53globalresolver.types.firewall_rules_fail_open_type
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.profile_resource_status
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class SharedDNSViewSummary(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the DNS view.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the DNS view.</p>"""
    client_token: "capo_route53globalresolver.types.client_token.ClientToken"
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dnssec_validation: (
        "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    )
    """<p>Whether DNSSEC validation is enabled for the DNS view.</p>"""
    edns_client_subnet: (
        "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    )
    """<p>Whether EDNS Client Subnet injection is enabled for the DNS view.</p>"""
    firewall_rules_fail_open: "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    """<p>Whether firewall rules fail open when they cannot be evaluated.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the DNS view.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the DNS view.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the global resolver that the DNS view is associated with.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the DNS view was created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the DNS view was last updated.</p>"""
    status: (
        "capo_route53globalresolver.types.profile_resource_status.ProfileResourceStatus"
    )
    """<p>The current status of the DNS view.</p>"""
    owner_account_id: "capo_route53globalresolver.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that owns the DNS view and shared it with your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharedDNSViewSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clientToken"] = value["client_token"]
    import capo_route53globalresolver.types.dns_sec_validation_type

    out["dnssecValidation"] = (
        capo_route53globalresolver.types.dns_sec_validation_type.serialize_json(
            value["dnssec_validation"]
        )
    )
    import capo_route53globalresolver.types.edns_client_subnet_type

    out["ednsClientSubnet"] = (
        capo_route53globalresolver.types.edns_client_subnet_type.serialize_json(
            value["edns_client_subnet"]
        )
    )
    import capo_route53globalresolver.types.firewall_rules_fail_open_type

    out["firewallRulesFailOpen"] = (
        capo_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
            value["firewall_rules_fail_open"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["globalResolverId"] = value["global_resolver_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import capo_route53globalresolver.types.profile_resource_status

    out["status"] = (
        capo_route53globalresolver.types.profile_resource_status.serialize_json(
            value["status"]
        )
    )
    out["ownerAccountId"] = value["owner_account_id"]
    return out


def deserialize_json(data: dict) -> SharedDNSViewSummary:
    out: SharedDNSViewSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SharedDNSViewSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SharedDNSViewSummary.arn required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("SharedDNSViewSummary.client_token required")
    if data.get("dnssecValidation") is not None:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    else:
        raise DeserializationError("SharedDNSViewSummary.dnssec_validation required")
    if data.get("ednsClientSubnet") is not None:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    else:
        raise DeserializationError("SharedDNSViewSummary.edns_client_subnet required")
    if data.get("firewallRulesFailOpen") is not None:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    else:
        raise DeserializationError(
            "SharedDNSViewSummary.firewall_rules_fail_open required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SharedDNSViewSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("globalResolverId") is not None:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError("SharedDNSViewSummary.global_resolver_id required")
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SharedDNSViewSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("SharedDNSViewSummary.updated_at required")
    if data.get("status") is not None:
        import capo_route53globalresolver.types.profile_resource_status

        out["status"] = (
            capo_route53globalresolver.types.profile_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("SharedDNSViewSummary.status required")
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        raise DeserializationError("SharedDNSViewSummary.owner_account_id required")
    return out
