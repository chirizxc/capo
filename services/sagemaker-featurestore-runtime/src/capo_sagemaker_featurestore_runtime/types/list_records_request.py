"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ListRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.boolean
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.list_records_max_results
    import capo_sagemaker_featurestore_runtime.types.list_records_next_token


class ListRecordsRequest(TypedDict, closed=True):
    feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the feature group to list records from.</p>"""
    max_results: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.list_records_max_results.ListRecordsMaxResults"
    ]
    """<p>The maximum number of record identifiers to return in a single page of results. For the <code>InMemory</code> tier, this value is a hint and not a strict requirement. The response may contain more or fewer results than the specified <code>MaxResults</code>.</p>"""
    next_token: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.list_records_next_token.ListRecordsNextToken"
    ]
    """<p>A token to resume pagination of <code>ListRecords</code> results.</p>"""
    include_soft_deleted_records: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.boolean.Boolean"
    ]
    """<p>If set to <code>true</code>, the result includes records that have been soft deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "include_soft_deleted_records" in value:
        out["IncludeSoftDeletedRecords"] = value["include_soft_deleted_records"]
    return out


def deserialize_json(data: dict) -> ListRecordsRequest:
    out: ListRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("IncludeSoftDeletedRecords") is not None:
        out["include_soft_deleted_records"] = data["IncludeSoftDeletedRecords"]
    return out
