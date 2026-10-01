"""Generated from Smithy shape ``com.amazonaws.quicksight#ListLimitsProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.list_limits_profiles_request_max_results_integer
    import capo_quicksight.types.resource_type


class ListLimitsProfilesRequest(TypedDict, closed=True):
    account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the limits profiles.</p>"""
    resource_type: NotRequired["capo_quicksight.types.resource_type.ResourceType"]
    """<p>An optional filter that limits the results to profiles that contain the specified resource type. If you don't specify a value, the operation returns all profiles.</p>"""
    max_results: NotRequired[
        "capo_quicksight.types.list_limits_profiles_request_max_results_integer.ListLimitsProfilesRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return in a single call. If you don't specify a value, the service uses the default maximum.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLimitsProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLimitsProfilesRequest:
    out: ListLimitsProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
