"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDlpSettingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dlp_setting_details


class DescribeDlpSettingResponse(TypedDict, closed=True):
    dlp_setting: "capo_quicksight.types.dlp_setting_details.DlpSettingDetails"
    """<p>The full configuration of the requested DLP setting, returned as a <code>DlpSettingDetails</code> object.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDlpSettingResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.dlp_setting_details

    out["DlpSetting"] = capo_quicksight.types.dlp_setting_details.serialize_json(
        value["dlp_setting"]
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDlpSettingResponse:
    out: DescribeDlpSettingResponse = {}  # type: ignore[typeddict-item]
    if data.get("DlpSetting") is not None:
        import capo_quicksight.types.dlp_setting_details

        out["dlp_setting"] = capo_quicksight.types.dlp_setting_details.deserialize_json(
            data["DlpSetting"]
        )
    else:
        raise DeserializationError("DescribeDlpSettingResponse.dlp_setting required")
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
