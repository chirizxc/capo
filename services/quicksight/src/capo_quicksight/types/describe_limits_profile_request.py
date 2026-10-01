"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeLimitsProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.profile_id


class DescribeLimitsProfileRequest(TypedDict, closed=True):
    profile_id: "capo_quicksight.types.profile_id.ProfileId"
    """<p>The unique identifier for the limits profile.</p>"""
    account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the limits profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLimitsProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeLimitsProfileRequest:
    out: DescribeLimitsProfileRequest = {}  # type: ignore[typeddict-item]
    return out
