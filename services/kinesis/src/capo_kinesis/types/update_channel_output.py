"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateChannelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.channel_description


class UpdateChannelOutput(TypedDict, closed=True):
    channel_description: "capo_kinesis.types.channel_description.ChannelDescription"
    """<p>The configuration and current status of the channel after the update, including its ARN, destination configuration, and lifecycle state. Immediately after the request, the state is <code>UPDATING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChannelOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.channel_description

    out["ChannelDescription"] = (
        capo_kinesis.types.channel_description.serialize_aws_json_1_1(
            value["channel_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChannelOutput:
    out: UpdateChannelOutput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelDescription") is not None:
        import capo_kinesis.types.channel_description

        out["channel_description"] = (
            capo_kinesis.types.channel_description.deserialize_aws_json_1_1(
                data["ChannelDescription"]
            )
        )
    else:
        raise DeserializationError("UpdateChannelOutput.channel_description required")
    return out
