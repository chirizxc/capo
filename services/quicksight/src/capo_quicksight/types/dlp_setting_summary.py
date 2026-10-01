"""Generated from Smithy shape ``com.amazonaws.quicksight#DlpSettingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dlp_provider_type
    import capo_quicksight.types.dlp_setting_id
    import capo_quicksight.types.dlp_setting_name
    import capo_quicksight.types.dlp_setting_status
    import capo_quicksight.types.timestamp


class DlpSettingSummary(TypedDict, closed=True):
    dlp_setting_id: "capo_quicksight.types.dlp_setting_id.DlpSettingId"
    """<p>The ID of the DLP setting.</p>"""
    name: "capo_quicksight.types.dlp_setting_name.DlpSettingName"
    """<p>The display name of the DLP setting.</p>"""
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DLP setting.</p>"""
    status: "capo_quicksight.types.dlp_setting_status.DlpSettingStatus"
    """<p>The status of the DLP setting. Valid values are <code>ACTIVE</code> and <code>INACTIVE</code>.</p>"""
    provider_type: "capo_quicksight.types.dlp_provider_type.DlpProviderType"
    """<p>The type of external DLP provider used for sensitivity label classification.</p>"""
    created_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the DLP setting was created, in ISO 8601 format.</p>"""
    updated_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the DLP setting was most recently updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DlpSettingSummary) -> dict:
    out: dict = {}
    out["DlpSettingId"] = value["dlp_setting_id"]
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    import capo_quicksight.types.dlp_setting_status

    out["Status"] = capo_quicksight.types.dlp_setting_status.serialize_json(
        value["status"]
    )
    import capo_quicksight.types.dlp_provider_type

    out["ProviderType"] = capo_quicksight.types.dlp_provider_type.serialize_json(
        value["provider_type"]
    )
    import capo_quicksight.types.timestamp

    out["CreatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_quicksight.types.timestamp

    out["UpdatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DlpSettingSummary:
    out: DlpSettingSummary = {}  # type: ignore[typeddict-item]
    if data.get("DlpSettingId") is not None:
        out["dlp_setting_id"] = data["DlpSettingId"]
    else:
        raise DeserializationError("DlpSettingSummary.dlp_setting_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DlpSettingSummary.name required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DlpSettingSummary.arn required")
    if data.get("Status") is not None:
        import capo_quicksight.types.dlp_setting_status

        out["status"] = capo_quicksight.types.dlp_setting_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("DlpSettingSummary.status required")
    if data.get("ProviderType") is not None:
        import capo_quicksight.types.dlp_provider_type

        out["provider_type"] = capo_quicksight.types.dlp_provider_type.deserialize_json(
            data["ProviderType"]
        )
    else:
        raise DeserializationError("DlpSettingSummary.provider_type required")
    if data.get("CreatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["created_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("DlpSettingSummary.created_at required")
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["updated_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("DlpSettingSummary.updated_at required")
    return out
