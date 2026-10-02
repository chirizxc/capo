"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobTrainingPlanArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_arn

OptimizationJobTrainingPlanArns: TypeAlias = list[
    "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobTrainingPlanArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OptimizationJobTrainingPlanArns:
    return [item for item in data if item is not None]
