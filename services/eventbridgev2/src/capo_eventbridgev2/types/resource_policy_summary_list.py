"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ResourcePolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.resource_policy_summary

ResourcePolicySummaryList: TypeAlias = list[
    "capo_eventbridgev2.types.resource_policy_summary.ResourcePolicySummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourcePolicySummaryList) -> list:
    import capo_eventbridgev2.types.resource_policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_eventbridgev2.types.resource_policy_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ResourcePolicySummaryList:
    import capo_eventbridgev2.types.resource_policy_summary

    out: ResourcePolicySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridgev2.types.resource_policy_summary.deserialize_cbor(item)
        )
    return out
