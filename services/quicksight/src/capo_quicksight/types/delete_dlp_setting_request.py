"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteDlpSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.dlp_setting_id


class DeleteDlpSettingRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the DLP setting that you want to delete.</p>"""
    dlp_setting_id: "capo_quicksight.types.dlp_setting_id.DlpSettingId"
    """<p>The ID of the DLP setting that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDlpSettingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDlpSettingRequest:
    out: DeleteDlpSettingRequest = {}  # type: ignore[typeddict-item]
    return out
