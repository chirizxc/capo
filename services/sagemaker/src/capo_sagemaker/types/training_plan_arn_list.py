"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_arn

TrainingPlanArnList: TypeAlias = list[
    "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TrainingPlanArnList:
    return [item for item in data if item is not None]
