"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.schedule_configuration
    import capo_customer_profiles.types.scheduled_executions
    import capo_customer_profiles.types.segment_subscription_status
    import capo_customer_profiles.types.string1_to1000
    import capo_customer_profiles.types.timestamp


class GetSegmentSubscriptionResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_customer_profiles.types.segment_subscription_status.SegmentSubscriptionStatus"
    ]
    """<p>The current lifecycle status of the subscription. The following are valid values: </p> <ul> <li> <p> <b>STARTING</b>: Initial snapshot is in progress. </p> </li> <li> <p> <b>RUNNING</b>: Notifications are active and running. </p> </li> <li> <p> <b>STOPPED</b>: Notifications have been stopped. </p> </li> <li> <p> <b>FAILED</b>: Notifications failed (for example, the Amazon Kinesis data stream became inaccessible). </p> </li> </ul>"""
    message: NotRequired["capo_customer_profiles.types.string1_to1000.string1To1000"]
    """<p>A status message providing additional context, such as a failure reason. </p>"""
    schedule_configuration: NotRequired[
        "capo_customer_profiles.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule configuration for periodic membership event notifications. </p>"""
    scheduled_executions: NotRequired[
        "capo_customer_profiles.types.scheduled_executions.ScheduledExecutions"
    ]
    """<p>Information about scheduled execution timestamps. </p>"""
    started_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the subscription was first started. </p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of the most recent configuration change. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentSubscriptionResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_customer_profiles.types.segment_subscription_status

        out["Status"] = (
            capo_customer_profiles.types.segment_subscription_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "schedule_configuration" in value:
        import capo_customer_profiles.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_customer_profiles.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    if "scheduled_executions" in value:
        import capo_customer_profiles.types.scheduled_executions

        out["ScheduledExecutions"] = (
            capo_customer_profiles.types.scheduled_executions.serialize_json(
                value["scheduled_executions"]
            )
        )
    if "started_at" in value:
        import capo_customer_profiles.types.timestamp

        out["StartedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetSegmentSubscriptionResponse:
    out: GetSegmentSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.segment_subscription_status

        out["status"] = (
            capo_customer_profiles.types.segment_subscription_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ScheduleConfiguration") is not None:
        import capo_customer_profiles.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_customer_profiles.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("ScheduledExecutions") is not None:
        import capo_customer_profiles.types.scheduled_executions

        out["scheduled_executions"] = (
            capo_customer_profiles.types.scheduled_executions.deserialize_json(
                data["ScheduledExecutions"]
            )
        )
    if data.get("StartedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["started_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["StartedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    return out
