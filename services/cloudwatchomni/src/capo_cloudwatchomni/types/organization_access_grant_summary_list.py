"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationAccessGrantSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.organization_access_grant_summary

OrganizationAccessGrantSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.organization_access_grant_summary.OrganizationAccessGrantSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationAccessGrantSummaryList) -> list:
    import capo_cloudwatchomni.types.organization_access_grant_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatchomni.types.organization_access_grant_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> OrganizationAccessGrantSummaryList:
    import capo_cloudwatchomni.types.organization_access_grant_summary

    out: OrganizationAccessGrantSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.organization_access_grant_summary.deserialize_cbor(
                item
            )
        )
    return out
