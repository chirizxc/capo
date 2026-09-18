"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkServiceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.account_id
    import capo_vpc_lattice.types.dns_entry
    import capo_vpc_lattice.types.service_arn
    import capo_vpc_lattice.types.service_custom_domain_name
    import capo_vpc_lattice.types.service_id
    import capo_vpc_lattice.types.service_name
    import capo_vpc_lattice.types.service_network_arn
    import capo_vpc_lattice.types.service_network_id
    import capo_vpc_lattice.types.service_network_name
    import capo_vpc_lattice.types.service_network_service_association_arn
    import capo_vpc_lattice.types.service_network_service_association_identifier
    import capo_vpc_lattice.types.service_network_service_association_status
    import capo_vpc_lattice.types.timestamp


class GetServiceNetworkServiceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier"
    ]
    """<p>The ID of the service network and service association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_service_association_status.ServiceNetworkServiceAssociationStatus"
    ]
    """<p>The status of the association.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_service_association_arn.ServiceNetworkServiceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    created_by: NotRequired["capo_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the association was created, in ISO-8601 format.</p>"""
    service_id: NotRequired["capo_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    service_name: NotRequired["capo_vpc_lattice.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    service_arn: NotRequired["capo_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    service_network_id: NotRequired[
        "capo_vpc_lattice.types.service_network_id.ServiceNetworkId"
    ]
    """<p>The ID of the service network.</p>"""
    service_network_name: NotRequired[
        "capo_vpc_lattice.types.service_network_name.ServiceNetworkName"
    ]
    """<p>The name of the service network.</p>"""
    service_network_arn: NotRequired[
        "capo_vpc_lattice.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    dns_entry: NotRequired["capo_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The DNS name of the service.</p>"""
    custom_domain_name: NotRequired[
        "capo_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
    ]
    """<p>The custom domain name of the service.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message.</p>"""
    failure_code: NotRequired["str"]
    """<p>The failure code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkServiceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "service_id" in value:
        out["serviceId"] = value["service_id"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_network_id" in value:
        out["serviceNetworkId"] = value["service_network_id"]
    if "service_network_name" in value:
        out["serviceNetworkName"] = value["service_network_name"]
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "dns_entry" in value:
        import capo_vpc_lattice.types.dns_entry

        out["dnsEntry"] = capo_vpc_lattice.types.dns_entry.serialize_json(
            value["dns_entry"]
        )
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> GetServiceNetworkServiceAssociationResponse:
    out: GetServiceNetworkServiceAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("createdAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("serviceId") is not None:
        out["service_id"] = data["serviceId"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("serviceNetworkId") is not None:
        out["service_network_id"] = data["serviceNetworkId"]
    if data.get("serviceNetworkName") is not None:
        out["service_network_name"] = data["serviceNetworkName"]
    if data.get("serviceNetworkArn") is not None:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if data.get("dnsEntry") is not None:
        import capo_vpc_lattice.types.dns_entry

        out["dns_entry"] = capo_vpc_lattice.types.dns_entry.deserialize_json(
            data["dnsEntry"]
        )
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    return out
