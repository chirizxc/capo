"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageFailureContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_failure_context
    import capo_imagebuilder.types.distribution_failure_context
    import capo_imagebuilder.types.image_status
    import capo_imagebuilder.types.workflow_build_version_arn
    import capo_imagebuilder.types.workflow_execution_id
    import capo_imagebuilder.types.workflow_step_execution_id
    import capo_imagebuilder.types.workflow_step_name


class ImageFailureContext(TypedDict, closed=True):
    image_status: NotRequired["capo_imagebuilder.types.image_status.ImageStatus"]
    """<p>The status that the image had when the failure occurred. This indicates the stage of the image creation process where the image failed, for example <code>BUILDING</code> or <code>DISTRIBUTING</code>.</p>"""
    workflow_execution_id: NotRequired[
        "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    ]
    """<p>The unique identifier of the workflow execution that was running when the image failed.</p>"""
    workflow_arn: NotRequired[
        "capo_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow build version that was running when the image failed.</p>"""
    step_execution_id: NotRequired[
        "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    ]
    """<p>The unique identifier of the workflow step execution that failed.</p>"""
    failed_step: NotRequired[
        "capo_imagebuilder.types.workflow_step_name.WorkflowStepName"
    ]
    """<p>The name of the workflow step that failed, as it appears in the workflow document.</p>"""
    component_failure: NotRequired[
        "capo_imagebuilder.types.component_failure_context.ComponentFailureContext"
    ]
    """<p>The details about the component that failed, if the failure occurred while a component was running.</p>"""
    distribution_failure: NotRequired[
        "capo_imagebuilder.types.distribution_failure_context.DistributionFailureContext"
    ]
    """<p>The details about the distribution failure, if the failure occurred while Image Builder distributed or configured the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageFailureContext) -> dict:
    out: dict = {}
    if "image_status" in value:
        import capo_imagebuilder.types.image_status

        out["imageStatus"] = capo_imagebuilder.types.image_status.serialize_json(
            value["image_status"]
        )
    if "workflow_execution_id" in value:
        out["workflowExecutionId"] = value["workflow_execution_id"]
    if "workflow_arn" in value:
        out["workflowArn"] = value["workflow_arn"]
    if "step_execution_id" in value:
        out["stepExecutionId"] = value["step_execution_id"]
    if "failed_step" in value:
        out["failedStep"] = value["failed_step"]
    if "component_failure" in value:
        import capo_imagebuilder.types.component_failure_context

        out["componentFailure"] = (
            capo_imagebuilder.types.component_failure_context.serialize_json(
                value["component_failure"]
            )
        )
    if "distribution_failure" in value:
        import capo_imagebuilder.types.distribution_failure_context

        out["distributionFailure"] = (
            capo_imagebuilder.types.distribution_failure_context.serialize_json(
                value["distribution_failure"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageFailureContext:
    out: ImageFailureContext = {}  # type: ignore[typeddict-item]
    if data.get("imageStatus") is not None:
        import capo_imagebuilder.types.image_status

        out["image_status"] = capo_imagebuilder.types.image_status.deserialize_json(
            data["imageStatus"]
        )
    if data.get("workflowExecutionId") is not None:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    if data.get("workflowArn") is not None:
        out["workflow_arn"] = data["workflowArn"]
    if data.get("stepExecutionId") is not None:
        out["step_execution_id"] = data["stepExecutionId"]
    if data.get("failedStep") is not None:
        out["failed_step"] = data["failedStep"]
    if data.get("componentFailure") is not None:
        import capo_imagebuilder.types.component_failure_context

        out["component_failure"] = (
            capo_imagebuilder.types.component_failure_context.deserialize_json(
                data["componentFailure"]
            )
        )
    if data.get("distributionFailure") is not None:
        import capo_imagebuilder.types.distribution_failure_context

        out["distribution_failure"] = (
            capo_imagebuilder.types.distribution_failure_context.deserialize_json(
                data["distributionFailure"]
            )
        )
    return out
