"""Generated from Smithy shape ``com.amazonaws.kinesis#ListChannelsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.list_channels_input_limit
    import capo_kinesis.types.next_token
    import capo_kinesis.types.stream_filter_list


class ListChannelsInput(TypedDict, closed=True):
    stream_filter: NotRequired["capo_kinesis.types.stream_filter_list.StreamFilterList"]
    """<p>Filters the results to channels associated with the specified streams.</p>"""
    max_results: NotRequired[
        "capo_kinesis.types.list_channels_input_limit.ListChannelsInputLimit"
    ]
    """<p>The maximum number of channels to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>The pagination token returned by a previous call. Specify this token to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListChannelsInput) -> dict:
    out: dict = {}
    if "stream_filter" in value:
        import capo_kinesis.types.stream_filter_list

        out["StreamFilter"] = (
            capo_kinesis.types.stream_filter_list.serialize_aws_json_1_1(
                value["stream_filter"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListChannelsInput:
    out: ListChannelsInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamFilter") is not None:
        import capo_kinesis.types.stream_filter_list

        out["stream_filter"] = (
            capo_kinesis.types.stream_filter_list.deserialize_aws_json_1_1(
                data["StreamFilter"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
