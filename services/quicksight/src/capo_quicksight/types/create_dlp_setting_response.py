"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateDlpSettingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dlp_setting_id


class CreateDlpSettingResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the created DLP setting.</p>"""
    dlp_setting_id: "capo_quicksight.types.dlp_setting_id.DlpSettingId"
    """<p>The ID of the created DLP setting.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDlpSettingResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["DlpSettingId"] = value["dlp_setting_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateDlpSettingResponse:
    out: CreateDlpSettingResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateDlpSettingResponse.arn required")
    if data.get("DlpSettingId") is not None:
        out["dlp_setting_id"] = data["DlpSettingId"]
    else:
        raise DeserializationError("CreateDlpSettingResponse.dlp_setting_id required")
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
