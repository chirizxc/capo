"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSoftwareInstanceGroupSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.image_release_version


class UpdateClusterSoftwareInstanceGroupSpecification(TypedDict, closed=True):
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group to update.</p>"""
    image_release_version: NotRequired[
        "capo_sagemaker.types.image_release_version.ImageReleaseVersion"
    ]
    """<p>The version of the HyperPod-managed AMI to update to for the instance group. Uses semantic versioning in the format <code>MAJOR.MINOR.PATCH</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateClusterSoftwareInstanceGroupSpecification,
) -> dict:
    out: dict = {}
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "image_release_version" in value:
        out["ImageReleaseVersion"] = value["image_release_version"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateClusterSoftwareInstanceGroupSpecification:
    out: UpdateClusterSoftwareInstanceGroupSpecification = {}  # type: ignore[typeddict-item]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    if data.get("ImageReleaseVersion") is not None:
        out["image_release_version"] = data["ImageReleaseVersion"]
    return out
