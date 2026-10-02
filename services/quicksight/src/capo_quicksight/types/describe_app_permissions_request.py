"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAppPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.app_id
    import capo_quicksight.types.aws_account_id


class DescribeAppPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the app.</p>"""
    app_id: "capo_quicksight.types.app_id.AppId"
    """<p>The ID of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppPermissionsRequest:
    out: DescribeAppPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
