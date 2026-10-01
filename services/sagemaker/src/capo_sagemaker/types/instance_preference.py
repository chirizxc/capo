"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_instance_count
    import capo_sagemaker.types.training_instance_type
    import capo_sagemaker.types.training_plan_arn_list


class InstancePreference(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.training_instance_type.TrainingInstanceType"
    ]
    """<p>The ML compute instance type. An instance type can appear only once in an <code>InstancePreferences</code> list.</p>"""
    instance_count: NotRequired[
        "capo_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>The number of instances to launch if this instance type is selected. Specify the instance count for the training job in one of the following two ways:</p> <ol> <li> <p> <b>Per preference</b> – Set <code>InstanceCount</code> on every preference in the <code>InstancePreferences</code> list and don't set <code>ResourceConfig$InstanceCount</code>. Use this when each instance type needs a different number of instances to deliver equivalent compute.</p> </li> <li> <p> <b>One count for the job</b> – Set <code>ResourceConfig$InstanceCount</code> and omit it from every preference. SageMaker applies this to all instance types in the list.</p> </li> </ol> <p>For example, in a list of five preferences, either all five specify <code>InstanceCount</code> or none of them do. SageMaker rejects requests that set <code>InstanceCount</code> on only some preferences, that set it both per preference and in <code>ResourceConfig</code>, or that omit it in both places.</p>"""
    training_plan_arns: NotRequired[
        "capo_sagemaker.types.training_plan_arn_list.TrainingPlanArnList"
    ]
    """<p>The Amazon Resource Name (ARN) of a training plan to use if this instance type is selected. The plan's instance type must match <code>InstanceType</code>. A preference with a training plan uses that plan's reserved capacity; a preference without one uses on-demand capacity. Per-preference <code>TrainingPlanArns</code> is mutually exclusive with the job-level <code>TrainingPlanArn</code> in <code>ResourceConfig</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePreference) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.training_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.training_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "training_plan_arns" in value:
        import capo_sagemaker.types.training_plan_arn_list

        out["TrainingPlanArns"] = (
            capo_sagemaker.types.training_plan_arn_list.serialize_aws_json_1_1(
                value["training_plan_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePreference:
    out: InstancePreference = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.training_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("TrainingPlanArns") is not None:
        import capo_sagemaker.types.training_plan_arn_list

        out["training_plan_arns"] = (
            capo_sagemaker.types.training_plan_arn_list.deserialize_aws_json_1_1(
                data["TrainingPlanArns"]
            )
        )
    return out
