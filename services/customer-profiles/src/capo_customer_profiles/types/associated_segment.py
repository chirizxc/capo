"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AssociatedSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_subscription_segment_status
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to1000


class AssociatedSegment(TypedDict, closed=True):
    segment_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the segment definition. </p>"""
    status: NotRequired[
        "capo_customer_profiles.types.event_subscription_segment_status.EventSubscriptionSegmentStatus"
    ]
    """<p>The subscription status of the segment. The following are valid values: </p> <ul> <li> <p> <b>STARTING</b>: The segment is being prepared to publish membership events. </p> </li> <li> <p> <b>RUNNING</b>: The segment is actively publishing membership events to the stream. </p> </li> <li> <p> <b>STOPPED</b>: The segment has stopped publishing membership events. </p> </li> <li> <p> <b>FAILED</b>: The segment failed to publish membership events. </p> </li> </ul>"""
    message: NotRequired["capo_customer_profiles.types.string1_to1000.string1To1000"]
    """<p>An optional message providing context, such as a failure reason. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSegment) -> dict:
    out: dict = {}
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "status" in value:
        import capo_customer_profiles.types.event_subscription_segment_status

        out["Status"] = (
            capo_customer_profiles.types.event_subscription_segment_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssociatedSegment:
    out: AssociatedSegment = {}  # type: ignore[typeddict-item]
    if data.get("SegmentName") is not None:
        out["segment_name"] = data["SegmentName"]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.event_subscription_segment_status

        out["status"] = (
            capo_customer_profiles.types.event_subscription_segment_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
