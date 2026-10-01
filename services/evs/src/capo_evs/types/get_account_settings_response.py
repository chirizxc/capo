"""Generated from Smithy shape ``com.amazonaws.evs#GetAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.account_setting_list


class GetAccountSettingsResponse(TypedDict, closed=True):
    settings: NotRequired["capo_evs.types.account_setting_list.AccountSettingList"]
    """<p>A list of regional account-level EVS settings for the account. EVS settings that have never been explicitly set are omitted from the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountSettingsResponse) -> dict:
    out: dict = {}
    if "settings" in value:
        import capo_evs.types.account_setting_list

        out["settings"] = capo_evs.types.account_setting_list.serialize_aws_json_1_0(
            value["settings"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountSettingsResponse:
    out: GetAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_evs.types.account_setting_list

        out["settings"] = capo_evs.types.account_setting_list.deserialize_aws_json_1_0(
            data["settings"]
        )
    return out
