"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_preference

InstancePreferenceList: TypeAlias = list[
    "capo_sagemaker.types.instance_preference.InstancePreference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePreferenceList) -> list:
    import capo_sagemaker.types.instance_preference

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.instance_preference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePreferenceList:
    import capo_sagemaker.types.instance_preference

    out: InstancePreferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.instance_preference.deserialize_aws_json_1_1(item)
        )
    return out
