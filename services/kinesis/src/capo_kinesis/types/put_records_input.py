"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.put_records_request_entry_list
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class PutRecordsInput(TypedDict, closed=True):
    records: (
        "capo_kinesis.types.put_records_request_entry_list.PutRecordsRequestEntryList"
    )
    """<p>The records associated with the request.</p>"""
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The stream name associated with the request.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsInput) -> dict:
    out: dict = {}
    import capo_kinesis.types.put_records_request_entry_list

    out["Records"] = (
        capo_kinesis.types.put_records_request_entry_list.serialize_aws_json_1_1(
            value["records"]
        )
    )
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordsInput:
    out: PutRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("Records") is not None:
        import capo_kinesis.types.put_records_request_entry_list

        out["records"] = (
            capo_kinesis.types.put_records_request_entry_list.deserialize_aws_json_1_1(
                data["Records"]
            )
        )
    else:
        raise DeserializationError("PutRecordsInput.records required")
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
