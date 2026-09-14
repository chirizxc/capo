"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileCachesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_cache_ids
    import capo_fsx.types.max_results
    import capo_fsx.types.next_token


class DescribeFileCachesRequest(TypedDict, closed=True):
    file_cache_ids: NotRequired["capo_fsx.types.file_cache_ids.FileCacheIds"]
    """<p>IDs of the caches whose descriptions you want to retrieve (String).</p>"""
    max_results: NotRequired["capo_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileCachesRequest) -> dict:
    out: dict = {}
    if "file_cache_ids" in value:
        import capo_fsx.types.file_cache_ids

        out["FileCacheIds"] = capo_fsx.types.file_cache_ids.serialize_aws_json_1_1(
            value["file_cache_ids"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileCachesRequest:
    out: DescribeFileCachesRequest = {}  # type: ignore[typeddict-item]
    if data.get("FileCacheIds") is not None:
        import capo_fsx.types.file_cache_ids

        out["file_cache_ids"] = capo_fsx.types.file_cache_ids.deserialize_aws_json_1_1(
            data["FileCacheIds"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
