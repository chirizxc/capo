"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDlpSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.pagination_token


class ListDlpSettingsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the DLP settings that you want to list.</p>"""
    next_token: NotRequired["capo_quicksight.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDlpSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDlpSettingsRequest:
    out: ListDlpSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
