"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ResourceDeploymentType``."""

from typing import Literal, TypeAlias, cast

ResourceDeploymentType: TypeAlias = Literal[
    "SINGLE_AZ",
    "WITH_MULTIAZ_STANDBY",
    "MULTI_NODE_READ_REPLICAS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDeploymentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceDeploymentType:
    return cast(ResourceDeploymentType, data)
