"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListSubscribersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.next_token
    import capo_eventbridgev2.types.subscriber_summary_list


class ListSubscribersResponse(TypedDict, closed=True):
    subscribers: NotRequired[
        "capo_eventbridgev2.types.subscriber_summary_list.SubscriberSummaryList"
    ]
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSubscribersResponse) -> dict:
    out: dict = {}
    if "subscribers" in value:
        import capo_eventbridgev2.types.subscriber_summary_list

        out["Subscribers"] = (
            capo_eventbridgev2.types.subscriber_summary_list.serialize_cbor(
                value["subscribers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSubscribersResponse:
    out: ListSubscribersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Subscribers") is not None:
        import capo_eventbridgev2.types.subscriber_summary_list

        out["subscribers"] = (
            capo_eventbridgev2.types.subscriber_summary_list.deserialize_cbor(
                data["Subscribers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
