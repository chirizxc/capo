"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutSegmentSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.schedule_configuration
    import capo_customer_profiles.types.segment_subscription_status
    import capo_customer_profiles.types.timestamp


class PutSegmentSubscriptionResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_customer_profiles.types.segment_subscription_status.SegmentSubscriptionStatus"
    ]
    """<p>The current lifecycle status of the subscription. The following are valid values: </p> <ul> <li> <p> <b>STARTING</b>: Initial snapshot is in progress. </p> </li> <li> <p> <b>RUNNING</b>: Notifications are active and running. </p> </li> <li> <p> <b>STOPPED</b>: Notifications have been stopped. </p> </li> <li> <p> <b>FAILED</b>: Notifications failed (for example, the Amazon Kinesis data stream became inaccessible). </p> </li> </ul>"""
    schedule_configuration: NotRequired[
        "capo_customer_profiles.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule configuration for the subscription, if configured. </p>"""
    started_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the subscription was started. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSegmentSubscriptionResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_customer_profiles.types.segment_subscription_status

        out["Status"] = (
            capo_customer_profiles.types.segment_subscription_status.serialize_json(
                value["status"]
            )
        )
    if "schedule_configuration" in value:
        import capo_customer_profiles.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_customer_profiles.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    if "started_at" in value:
        import capo_customer_profiles.types.timestamp

        out["StartedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["started_at"]
        )
    return out


def deserialize_json(data: dict) -> PutSegmentSubscriptionResponse:
    out: PutSegmentSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.segment_subscription_status

        out["status"] = (
            capo_customer_profiles.types.segment_subscription_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ScheduleConfiguration") is not None:
        import capo_customer_profiles.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_customer_profiles.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("StartedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["started_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["StartedAt"]
        )
    return out
