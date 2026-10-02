"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingResourceType``."""

from typing import Literal, TypeAlias, cast

FindingResourceType: TypeAlias = Literal[
    "EC2_INSTANCE",
    "EC2_NETWORK_INTERFACE",
    "S3_BUCKET",
    "S3_OBJECT",
    "ACCESS_KEY",
    "EKS_CLUSTER",
    "KUBERNETES_WORKLOAD",
    "CONTAINER",
    "ECS_CLUSTER",
    "ECS_TASK",
    "AUTOSCALING_AUTO_SCALING_GROUP",
    "IAM_INSTANCE_PROFILE",
    "CLOUDFORMATION_STACK",
    "EC2_LAUNCH_TEMPLATE",
    "EC2_VPC",
    "EC2_IMAGE",
    "BEDROCK_CUSTOM_MODEL",
    "BEDROCK_IMPORTED_MODEL",
    "BEDROCK_PROVISIONED_MODEL",
    "BEDROCK_CUSTOM_MODEL_DEPLOYMENT",
    "BEDROCK_INFERENCE_PROFILE",
    "BEDROCK_APPLICATION_INFERENCE_PROFILE",
    "BEDROCK_PROMPT",
    "BEDROCK_PROMPT_ROUTER",
    "BEDROCK_GUARDRAIL",
    "SAGEMAKER_ENDPOINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingResourceType) -> str:
    return value


def deserialize_json(data: str) -> FindingResourceType:
    return cast(FindingResourceType, data)
