"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#SharedDNSViews``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.shared_dns_view_summary

SharedDNSViews: TypeAlias = list[
    "capo_route53globalresolver.types.shared_dns_view_summary.SharedDNSViewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedDNSViews) -> list:
    import capo_route53globalresolver.types.shared_dns_view_summary

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.shared_dns_view_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SharedDNSViews:
    import capo_route53globalresolver.types.shared_dns_view_summary

    out: SharedDNSViews = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route53globalresolver.types.shared_dns_view_summary.deserialize_json(
                item
            )
        )
    return out
