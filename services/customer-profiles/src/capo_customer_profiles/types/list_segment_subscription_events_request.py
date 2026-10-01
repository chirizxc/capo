"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListSegmentSubscriptionEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListSegmentSubscriptionEventsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition. </p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of events to return per page. </p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSegmentSubscriptionEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSegmentSubscriptionEventsRequest:
    out: ListSegmentSubscriptionEventsRequest = {}  # type: ignore[typeddict-item]
    return out
