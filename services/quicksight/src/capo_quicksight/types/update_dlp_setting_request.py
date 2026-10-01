"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDlpSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.dlp_action
    import capo_quicksight.types.dlp_provider_type
    import capo_quicksight.types.dlp_setting_id
    import capo_quicksight.types.dlp_setting_name
    import capo_quicksight.types.provider_config


class UpdateDlpSettingRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the DLP setting that you want to update.</p>"""
    dlp_setting_id: "capo_quicksight.types.dlp_setting_id.DlpSettingId"
    """<p>The ID of the DLP setting that you want to update.</p>"""
    name: NotRequired["capo_quicksight.types.dlp_setting_name.DlpSettingName"]
    """<p>An updated display name for the DLP setting.</p>"""
    provider_type: NotRequired[
        "capo_quicksight.types.dlp_provider_type.DlpProviderType"
    ]
    """<p>An updated DLP provider type. Currently, the only supported value is <code>MICROSOFT_PURVIEW</code>.</p>"""
    provider_config: NotRequired["capo_quicksight.types.provider_config.ProviderConfig"]
    """<p>An updated provider-specific configuration for the DLP integration. This is a union type structure. For this structure to be valid, only one of the attributes can be defined.</p>"""
    provider_outage_action: NotRequired["capo_quicksight.types.dlp_action.DlpAction"]
    """<p>An updated behavior to apply when the DLP provider is unreachable. Valid values are <code>ALLOW</code>, <code>WARN</code>, and <code>BLOCK</code>.</p>"""
    enabled: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Specifies whether DLP enforcement is active for this setting. Set to <code>true</code> to enable enforcement, or <code>false</code> to disable it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDlpSettingRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "provider_type" in value:
        import capo_quicksight.types.dlp_provider_type

        out["ProviderType"] = capo_quicksight.types.dlp_provider_type.serialize_json(
            value["provider_type"]
        )
    if "provider_config" in value:
        import capo_quicksight.types.provider_config

        out["ProviderConfig"] = capo_quicksight.types.provider_config.serialize_json(
            value["provider_config"]
        )
    if "provider_outage_action" in value:
        import capo_quicksight.types.dlp_action

        out["ProviderOutageAction"] = capo_quicksight.types.dlp_action.serialize_json(
            value["provider_outage_action"]
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> UpdateDlpSettingRequest:
    out: UpdateDlpSettingRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ProviderType") is not None:
        import capo_quicksight.types.dlp_provider_type

        out["provider_type"] = capo_quicksight.types.dlp_provider_type.deserialize_json(
            data["ProviderType"]
        )
    if data.get("ProviderConfig") is not None:
        import capo_quicksight.types.provider_config

        out["provider_config"] = capo_quicksight.types.provider_config.deserialize_json(
            data["ProviderConfig"]
        )
    if data.get("ProviderOutageAction") is not None:
        import capo_quicksight.types.dlp_action

        out["provider_outage_action"] = (
            capo_quicksight.types.dlp_action.deserialize_json(
                data["ProviderOutageAction"]
            )
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
