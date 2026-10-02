"""Generated from Smithy shape ``com.amazonaws.acm#DnsPrevalidationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_scope
    import capo_acm.types.hosted_zone_id


class DnsPrevalidationOptions(TypedDict, closed=True):
    domain_scope: NotRequired["capo_acm.types.domain_scope.DomainScope"]
    """<p>The scope of domains covered by this prevalidation.</p>"""
    hosted_zone_id: NotRequired["capo_acm.types.hosted_zone_id.HostedZoneId"]
    """<p>The Route 53 hosted zone ID for DNS validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsPrevalidationOptions) -> dict:
    out: dict = {}
    if "domain_scope" in value:
        import capo_acm.types.domain_scope

        out["DomainScope"] = capo_acm.types.domain_scope.serialize_aws_json_1_1(
            value["domain_scope"]
        )
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsPrevalidationOptions:
    out: DnsPrevalidationOptions = {}  # type: ignore[typeddict-item]
    if data.get("DomainScope") is not None:
        import capo_acm.types.domain_scope

        out["domain_scope"] = capo_acm.types.domain_scope.deserialize_aws_json_1_1(
            data["DomainScope"]
        )
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    return out
