"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListEventSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_source_summary_list
    import capo_eventbridgev2.types.next_token


class ListEventSourcesResponse(TypedDict, closed=True):
    event_sources: NotRequired[
        "capo_eventbridgev2.types.event_source_summary_list.EventSourceSummaryList"
    ]
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEventSourcesResponse) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import capo_eventbridgev2.types.event_source_summary_list

        out["EventSources"] = (
            capo_eventbridgev2.types.event_source_summary_list.serialize_cbor(
                value["event_sources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEventSourcesResponse:
    out: ListEventSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventSources") is not None:
        import capo_eventbridgev2.types.event_source_summary_list

        out["event_sources"] = (
            capo_eventbridgev2.types.event_source_summary_list.deserialize_cbor(
                data["EventSources"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
