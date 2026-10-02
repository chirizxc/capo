"""Generated from Smithy shape ``com.amazonaws.acm#DnsPrevalidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_scope
    import capo_acm.types.hosted_zone_id
    import capo_acm.types.resource_record


class DnsPrevalidationDetails(TypedDict, closed=True):
    domain_scope: NotRequired["capo_acm.types.domain_scope.DomainScope"]
    """<p>The scope of domains covered by this prevalidation.</p>"""
    hosted_zone_id: NotRequired["capo_acm.types.hosted_zone_id.HostedZoneId"]
    """<p>The Route 53 hosted zone ID for DNS validation.</p>"""
    resource_record: NotRequired["capo_acm.types.resource_record.ResourceRecord"]
    """<p>The DNS resource record to create for domain validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsPrevalidationDetails) -> dict:
    out: dict = {}
    if "domain_scope" in value:
        import capo_acm.types.domain_scope

        out["DomainScope"] = capo_acm.types.domain_scope.serialize_aws_json_1_1(
            value["domain_scope"]
        )
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    if "resource_record" in value:
        import capo_acm.types.resource_record

        out["ResourceRecord"] = capo_acm.types.resource_record.serialize_aws_json_1_1(
            value["resource_record"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsPrevalidationDetails:
    out: DnsPrevalidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("DomainScope") is not None:
        import capo_acm.types.domain_scope

        out["domain_scope"] = capo_acm.types.domain_scope.deserialize_aws_json_1_1(
            data["DomainScope"]
        )
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    if data.get("ResourceRecord") is not None:
        import capo_acm.types.resource_record

        out["resource_record"] = (
            capo_acm.types.resource_record.deserialize_aws_json_1_1(
                data["ResourceRecord"]
            )
        )
    return out
