"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutSegmentSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.schedule_configuration


class PutSegmentSubscriptionRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition. </p>"""
    schedule_configuration: NotRequired[
        "capo_customer_profiles.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The optional schedule configuration that controls how often membership snapshots are run. If not provided, the subscription defaults to a 24-hour interval. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSegmentSubscriptionRequest) -> dict:
    out: dict = {}
    if "schedule_configuration" in value:
        import capo_customer_profiles.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_customer_profiles.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSegmentSubscriptionRequest:
    out: PutSegmentSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleConfiguration") is not None:
        import capo_customer_profiles.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_customer_profiles.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    return out
