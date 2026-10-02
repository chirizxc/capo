"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.next_token
    import capo_eventbridgev2.types.resource_policy_summary_list


class ListResourcePoliciesResponse(TypedDict, closed=True):
    policy_summaries: NotRequired[
        "capo_eventbridgev2.types.resource_policy_summary_list.ResourcePolicySummaryList"
    ]
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "policy_summaries" in value:
        import capo_eventbridgev2.types.resource_policy_summary_list

        out["PolicySummaries"] = (
            capo_eventbridgev2.types.resource_policy_summary_list.serialize_cbor(
                value["policy_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListResourcePoliciesResponse:
    out: ListResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicySummaries") is not None:
        import capo_eventbridgev2.types.resource_policy_summary_list

        out["policy_summaries"] = (
            capo_eventbridgev2.types.resource_policy_summary_list.deserialize_cbor(
                data["PolicySummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
