"""Generated from Smithy shape ``com.amazonaws.evs#AccountSettingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.account_setting

AccountSettingList: TypeAlias = list["capo_evs.types.account_setting.AccountSetting"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSettingList) -> list:
    import capo_evs.types.account_setting

    out: list = []
    for item in value:
        out.append(capo_evs.types.account_setting.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AccountSettingList:
    import capo_evs.types.account_setting

    out: AccountSettingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_evs.types.account_setting.deserialize_aws_json_1_0(item))
    return out
