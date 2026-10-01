"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#OnFailureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.dead_letter_queue_arn


class OnFailureConfiguration(TypedDict, closed=True):
    arn: NotRequired[
        "capo_eventbridgev2.types.dead_letter_queue_arn.DeadLetterQueueArn"
    ]
    """The ARN of the destination that receives events that could not be delivered. An Amazon SQS queue is the supported destination."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OnFailureConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> OnFailureConfiguration:
    out: OnFailureConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
