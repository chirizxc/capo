"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListEventBusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_summary_list
    import capo_eventbridgev2.types.next_token


class ListEventBusesResponse(TypedDict, closed=True):
    event_buses: NotRequired[
        "capo_eventbridgev2.types.event_bus_summary_list.EventBusSummaryList"
    ]
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEventBusesResponse) -> dict:
    out: dict = {}
    if "event_buses" in value:
        import capo_eventbridgev2.types.event_bus_summary_list

        out["EventBuses"] = (
            capo_eventbridgev2.types.event_bus_summary_list.serialize_cbor(
                value["event_buses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEventBusesResponse:
    out: ListEventBusesResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventBuses") is not None:
        import capo_eventbridgev2.types.event_bus_summary_list

        out["event_buses"] = (
            capo_eventbridgev2.types.event_bus_summary_list.deserialize_cbor(
                data["EventBuses"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
