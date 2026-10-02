"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterPatchingStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>The strategy for applying automatic patches to instances.</p> <ul> <li> <p> <code>WhenIdle</code>: Cordons all instances and patches each instance as it becomes idle (no running jobs). Each instance is uncordoned immediately after patching and becomes available for new jobs. If instances do not become idle, they remain on the previous AMI version. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.</p> </li> <li> <p> <code>WhenAllIdle</code>: Cordons all instances and waits for all to become idle before patching. All instances are uncordoned after patching completes. If not all instances become idle, no patching occurs and all instances remain on the previous AMI version.</p> </li> </ul>"""
ClusterPatchingStrategy: TypeAlias = Literal[
    "WhenIdle",
    "WhenAllIdle",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterPatchingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterPatchingStrategy:
    return cast(ClusterPatchingStrategy, data)
