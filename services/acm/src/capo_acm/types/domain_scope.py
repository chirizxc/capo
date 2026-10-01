"""Generated from Smithy shape ``com.amazonaws.acm#DomainScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_scope_option


class DomainScope(TypedDict, closed=True):
    exact_domain: NotRequired["capo_acm.types.domain_scope_option.DomainScopeOption"]
    """<p>Whether validation applies to the exact domain.</p>"""
    subdomains: NotRequired["capo_acm.types.domain_scope_option.DomainScopeOption"]
    """<p>Whether validation applies to subdomains.</p>"""
    wildcards: NotRequired["capo_acm.types.domain_scope_option.DomainScopeOption"]
    """<p>Whether validation applies to wildcard domains.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainScope) -> dict:
    out: dict = {}
    if "exact_domain" in value:
        import capo_acm.types.domain_scope_option

        out["ExactDomain"] = capo_acm.types.domain_scope_option.serialize_aws_json_1_1(
            value["exact_domain"]
        )
    if "subdomains" in value:
        import capo_acm.types.domain_scope_option

        out["Subdomains"] = capo_acm.types.domain_scope_option.serialize_aws_json_1_1(
            value["subdomains"]
        )
    if "wildcards" in value:
        import capo_acm.types.domain_scope_option

        out["Wildcards"] = capo_acm.types.domain_scope_option.serialize_aws_json_1_1(
            value["wildcards"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainScope:
    out: DomainScope = {}  # type: ignore[typeddict-item]
    if data.get("ExactDomain") is not None:
        import capo_acm.types.domain_scope_option

        out["exact_domain"] = (
            capo_acm.types.domain_scope_option.deserialize_aws_json_1_1(
                data["ExactDomain"]
            )
        )
    if data.get("Subdomains") is not None:
        import capo_acm.types.domain_scope_option

        out["subdomains"] = capo_acm.types.domain_scope_option.deserialize_aws_json_1_1(
            data["Subdomains"]
        )
    if data.get("Wildcards") is not None:
        import capo_acm.types.domain_scope_option

        out["wildcards"] = capo_acm.types.domain_scope_option.deserialize_aws_json_1_1(
            data["Wildcards"]
        )
    return out
