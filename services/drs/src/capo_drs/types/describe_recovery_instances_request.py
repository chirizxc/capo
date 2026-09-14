"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoveryInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.describe_recovery_instances_request_filters
    import capo_drs.types.pagination_token
    import capo_drs.types.strictly_positive_integer


class DescribeRecoveryInstancesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_drs.types.describe_recovery_instances_request_filters.DescribeRecoveryInstancesRequestFilters"
    ]
    """<p>A set of filters by which to return Recovery Instances.</p>"""
    max_results: NotRequired[
        "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Maximum number of Recovery Instances to retrieve.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Recovery Instance to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryInstancesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_drs.types.describe_recovery_instances_request_filters

        out["filters"] = (
            capo_drs.types.describe_recovery_instances_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeRecoveryInstancesRequest:
    out: DescribeRecoveryInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_drs.types.describe_recovery_instances_request_filters

        out["filters"] = (
            capo_drs.types.describe_recovery_instances_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
