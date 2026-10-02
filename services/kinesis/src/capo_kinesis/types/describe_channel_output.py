"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeChannelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.channel_description


class DescribeChannelOutput(TypedDict, closed=True):
    channel_description: "capo_kinesis.types.channel_description.ChannelDescription"
    """<p>The configuration and current status of the channel, including its ARN, source stream, destination configuration, and lifecycle state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeChannelOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.channel_description

    out["ChannelDescription"] = (
        capo_kinesis.types.channel_description.serialize_aws_json_1_1(
            value["channel_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeChannelOutput:
    out: DescribeChannelOutput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelDescription") is not None:
        import capo_kinesis.types.channel_description

        out["channel_description"] = (
            capo_kinesis.types.channel_description.deserialize_aws_json_1_1(
                data["ChannelDescription"]
            )
        )
    else:
        raise DeserializationError("DescribeChannelOutput.channel_description required")
    return out
