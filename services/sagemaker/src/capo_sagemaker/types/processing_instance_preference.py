"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingInstancePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_instance_count
    import capo_sagemaker.types.processing_instance_type


class ProcessingInstancePreference(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.processing_instance_type.ProcessingInstanceType"
    ]
    """<p>The ML compute instance type. An instance type can appear only once in an <code>InstancePreferences</code> list.</p>"""
    instance_count: NotRequired[
        "capo_sagemaker.types.processing_instance_count.ProcessingInstanceCount"
    ]
    """<p>The number of instances to launch if this instance type is selected. Specify the instance count for the processing job in one of the following two ways:</p> <ol> <li> <p> <b>Per preference</b> – Set <code>InstanceCount</code> on every preference in the <code>InstancePreferences</code> list and don't set <code>ProcessingClusterConfig$InstanceCount</code>. Use this when each instance type needs a different number of instances to deliver equivalent compute.</p> </li> <li> <p> <b>One count for the job</b> – Set <code>ProcessingClusterConfig$InstanceCount</code> and omit it from every preference. Amazon SageMaker applies this to all instance types in the list.</p> </li> </ol> <p>For example, in a list of five preferences, either all five specify <code>InstanceCount</code> or none of them do. Amazon SageMaker rejects requests that set <code>InstanceCount</code> on only some preferences, that set it both per preference and in <code>ProcessingClusterConfig</code>, or that omit it in both places.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingInstancePreference) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.processing_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.processing_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingInstancePreference:
    out: ProcessingInstancePreference = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.processing_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.processing_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    return out
