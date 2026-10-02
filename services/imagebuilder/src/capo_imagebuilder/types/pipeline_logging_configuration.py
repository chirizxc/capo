"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PipelineLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.log_group_name


class PipelineLoggingConfiguration(TypedDict, closed=True):
    image_log_group_name: NotRequired[
        "capo_imagebuilder.types.log_group_name.LogGroupName"
    ]
    """<p>Specifies the CloudWatch Logs log group name for image build logs. The log group name can contain alphanumeric characters, hyphens, underscores, forward slashes, and periods, up to 512 characters. Log group names not starting with <code>/aws/imagebuilder/</code> require an <code>executionRole</code> with CloudWatch Logs write permissions. If not specified, defaults to <code>/aws/imagebuilder/image-name</code>.</p>"""
    pipeline_log_group_name: NotRequired[
        "capo_imagebuilder.types.log_group_name.LogGroupName"
    ]
    """<p>Specifies the CloudWatch Logs log group name for pipeline execution logs. The log group name can contain alphanumeric characters, hyphens, underscores, forward slashes, and periods, up to 512 characters. Log group names not starting with <code>/aws/imagebuilder/</code> require an <code>executionRole</code> with CloudWatch Logs write permissions. If not specified, defaults to <code>/aws/imagebuilder/pipeline/pipeline-name</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineLoggingConfiguration) -> dict:
    out: dict = {}
    if "image_log_group_name" in value:
        out["imageLogGroupName"] = value["image_log_group_name"]
    if "pipeline_log_group_name" in value:
        out["pipelineLogGroupName"] = value["pipeline_log_group_name"]
    return out


def deserialize_json(data: dict) -> PipelineLoggingConfiguration:
    out: PipelineLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageLogGroupName") is not None:
        out["image_log_group_name"] = data["imageLogGroupName"]
    if data.get("pipelineLogGroupName") is not None:
        out["pipeline_log_group_name"] = data["pipelineLogGroupName"]
    return out
