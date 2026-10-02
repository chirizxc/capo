"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.stream_filter

StreamFilterList: TypeAlias = list["capo_kinesis.types.stream_filter.StreamFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamFilterList) -> list:
    import capo_kinesis.types.stream_filter

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.stream_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StreamFilterList:
    import capo_kinesis.types.stream_filter

    out: StreamFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kinesis.types.stream_filter.deserialize_aws_json_1_1(item))
    return out
