"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DescribeSubscriberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.subscriber_arn


class DescribeSubscriberRequest(TypedDict, closed=True):
    subscriber_arn: "capo_eventbridgev2.types.subscriber_arn.SubscriberArn"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSubscriberRequest) -> dict:
    out: dict = {}
    out["SubscriberArn"] = value["subscriber_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeSubscriberRequest:
    out: DescribeSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubscriberArn") is not None:
        out["subscriber_arn"] = data["SubscriberArn"]
    else:
        raise DeserializationError("DescribeSubscriberRequest.subscriber_arn required")
    return out
