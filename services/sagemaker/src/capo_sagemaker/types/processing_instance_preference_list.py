"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingInstancePreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_instance_preference

ProcessingInstancePreferenceList: TypeAlias = list[
    "capo_sagemaker.types.processing_instance_preference.ProcessingInstancePreference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingInstancePreferenceList) -> list:
    import capo_sagemaker.types.processing_instance_preference

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.processing_instance_preference.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProcessingInstancePreferenceList:
    import capo_sagemaker.types.processing_instance_preference

    out: ProcessingInstancePreferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.processing_instance_preference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
