"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionCleanup``."""

from typing import Literal, TypeAlias, cast

"""<p>The time when Amazon ECS removes the source revisions' tasks relative to deployment completion. When set to <code>BLOCKING</code>, Amazon ECS removes the previous tasks before completing the deployment. When set to <code>DEFERRED</code>, Amazon ECS completes the deployment first and removes the previous tasks in the background.</p>"""
ServiceRevisionCleanup: TypeAlias = Literal[
    "BLOCKING",
    "DEFERRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionCleanup) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceRevisionCleanup:
    return cast(ServiceRevisionCleanup, data)
