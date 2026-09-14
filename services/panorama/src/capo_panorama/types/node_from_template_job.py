"""Generated from Smithy shape ``com.amazonaws.panorama#NodeFromTemplateJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.created_time
    import capo_panorama.types.job_id
    import capo_panorama.types.node_from_template_job_status
    import capo_panorama.types.node_from_template_job_status_message
    import capo_panorama.types.node_name
    import capo_panorama.types.template_type


class NodeFromTemplateJob(TypedDict, closed=True):
    job_id: NotRequired["capo_panorama.types.job_id.JobId"]
    """<p>The job's ID.</p>"""
    template_type: NotRequired["capo_panorama.types.template_type.TemplateType"]
    """<p>The job's template type.</p>"""
    status: NotRequired[
        "capo_panorama.types.node_from_template_job_status.NodeFromTemplateJobStatus"
    ]
    """<p>The job's status.</p>"""
    status_message: NotRequired[
        "capo_panorama.types.node_from_template_job_status_message.NodeFromTemplateJobStatusMessage"
    ]
    """<p>The job's status message.</p>"""
    created_time: NotRequired["capo_panorama.types.created_time.CreatedTime"]
    """<p>When the job was created.</p>"""
    node_name: NotRequired["capo_panorama.types.node_name.NodeName"]
    """<p>The node's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeFromTemplateJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "template_type" in value:
        out["TemplateType"] = value["template_type"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_time" in value:
        import capo_panorama.types.created_time

        out["CreatedTime"] = capo_panorama.types.created_time.serialize_json(
            value["created_time"]
        )
    if "node_name" in value:
        out["NodeName"] = value["node_name"]
    return out


def deserialize_json(data: dict) -> NodeFromTemplateJob:
    out: NodeFromTemplateJob = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("TemplateType") is not None:
        out["template_type"] = data["TemplateType"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreatedTime") is not None:
        import capo_panorama.types.created_time

        out["created_time"] = capo_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("NodeName") is not None:
        out["node_name"] = data["NodeName"]
    return out
