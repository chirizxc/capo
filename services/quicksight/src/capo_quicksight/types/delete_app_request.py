"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.app_id
    import capo_quicksight.types.aws_account_id


class DeleteAppRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the app.</p>"""
    app_id: "capo_quicksight.types.app_id.AppId"
    """<p>The ID of the app that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppRequest:
    out: DeleteAppRequest = {}  # type: ignore[typeddict-item]
    return out
