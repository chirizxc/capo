"""Generated from Smithy shape ``com.amazonaws.transfer#SecretVersionStageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.secret_version_stage

SecretVersionStageList: TypeAlias = list[
    "capo_transfer.types.secret_version_stage.SecretVersionStage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretVersionStageList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecretVersionStageList:
    return [item for item in data if item is not None]
