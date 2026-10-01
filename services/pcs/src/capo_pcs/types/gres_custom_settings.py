"""Generated from Smithy shape ``com.amazonaws.pcs#GresCustomSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.gres_custom_setting_map

GresCustomSettings: TypeAlias = list[
    "capo_pcs.types.gres_custom_setting_map.GresCustomSettingMap"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GresCustomSettings) -> list:
    import capo_pcs.types.gres_custom_setting_map

    out: list = []
    for item in value:
        out.append(capo_pcs.types.gres_custom_setting_map.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> GresCustomSettings:
    import capo_pcs.types.gres_custom_setting_map

    out: GresCustomSettings = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pcs.types.gres_custom_setting_map.deserialize_aws_json_1_0(item)
        )
    return out
