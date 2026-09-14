"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateRetrainingSchedulerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.retraining_scheduler_status


class CreateRetrainingSchedulerResponse(TypedDict, closed=True):
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the model that you added the retraining scheduler to. </p>"""
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The ARN of the model that you added the retraining scheduler to. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>The status of the retraining scheduler. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRetrainingSchedulerResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["Status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRetrainingSchedulerResponse:
    out: CreateRetrainingSchedulerResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.retraining_scheduler_status

        out["status"] = (
            capo_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
