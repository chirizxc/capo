"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetStreamForSegmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.associated_segments_list
    import capo_customer_profiles.types.destination_arn_string
    import capo_customer_profiles.types.destination_role_arn
    import capo_customer_profiles.types.event_subscription_state
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.timestamp


class GetStreamForSegmentsResponse(TypedDict, closed=True):
    associated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the stream was associated. </p>"""
    associated_segments: NotRequired[
        "capo_customer_profiles.types.associated_segments_list.AssociatedSegmentsList"
    ]
    """<p>A list of segments currently associated with the stream and their subscription status. </p>"""
    domain_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the domain.</p>"""
    destination_arn: NotRequired[
        "capo_customer_profiles.types.destination_arn_string.DestinationArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Kinesis data stream receiving segment membership events. </p>"""
    destination_role_arn: NotRequired[
        "capo_customer_profiles.types.destination_role_arn.DestinationRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role used for Amazon Kinesis and AWS Key Management Service (KMS) operations. </p>"""
    state: NotRequired[
        "capo_customer_profiles.types.event_subscription_state.EventSubscriptionState"
    ]
    """<p>The operational state of the destination stream. The following are valid values: </p> <ul> <li> <p> <b>RUNNING</b>: The stream is associated and healthy. Segment membership events are being published. </p> </li> <li> <p> <b>UNHEALTHY</b>: The stream is associated but events cannot currently be published. See <code>FailureReason</code> for details. </p> </li> <li> <p> <b>STOPPED</b>: The stream is no longer publishing segment membership events. </p> </li> </ul>"""
    disassociated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the stream was disassociated. </p>"""
    failure_reason: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The reason why the stream is in an unhealthy state, if applicable. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamForSegmentsResponse) -> dict:
    out: dict = {}
    if "associated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["AssociatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["associated_at"]
        )
    if "associated_segments" in value:
        import capo_customer_profiles.types.associated_segments_list

        out["AssociatedSegments"] = (
            capo_customer_profiles.types.associated_segments_list.serialize_json(
                value["associated_segments"]
            )
        )
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "destination_role_arn" in value:
        out["DestinationRoleArn"] = value["destination_role_arn"]
    if "state" in value:
        import capo_customer_profiles.types.event_subscription_state

        out["State"] = (
            capo_customer_profiles.types.event_subscription_state.serialize_json(
                value["state"]
            )
        )
    if "disassociated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["DisassociatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["disassociated_at"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetStreamForSegmentsResponse:
    out: GetStreamForSegmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["associated_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["AssociatedAt"]
        )
    if data.get("AssociatedSegments") is not None:
        import capo_customer_profiles.types.associated_segments_list

        out["associated_segments"] = (
            capo_customer_profiles.types.associated_segments_list.deserialize_json(
                data["AssociatedSegments"]
            )
        )
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    if data.get("DestinationRoleArn") is not None:
        out["destination_role_arn"] = data["DestinationRoleArn"]
    if data.get("State") is not None:
        import capo_customer_profiles.types.event_subscription_state

        out["state"] = (
            capo_customer_profiles.types.event_subscription_state.deserialize_json(
                data["State"]
            )
        )
    if data.get("DisassociatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["disassociated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["DisassociatedAt"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
