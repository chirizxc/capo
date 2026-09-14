"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsByConsumableResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.consumable_resource_properties
    import capo_batch.types.long
    import capo_batch.types.string


class ListJobsByConsumableResourceSummary(TypedDict, closed=True):
    job_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_queue_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job queue.</p>"""
    job_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the job.</p>"""
    job_definition_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition.</p>"""
    share_identifier: NotRequired["capo_batch.types.string.String"]
    """<p>The fair-share scheduling identifier for the job.</p>"""
    job_status: NotRequired["capo_batch.types.string.String"]
    """<p>The status of the job. Can be one of:</p> <ul> <li> <p> <code>SUBMITTED</code> </p> </li> <li> <p> <code>PENDING</code> </p> </li> <li> <p> <code>RUNNABLE</code> </p> </li> <li> <p> <code>STARTING</code> </p> </li> <li> <p> <code>RUNNING</code> </p> </li> <li> <p> <code>SUCCEEDED</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> </ul>"""
    quantity: NotRequired["capo_batch.types.long.Long"]
    """<p>The total amount of the consumable resource that is available.</p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the job.</p>"""
    started_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp for when the job was started. More specifically, it's when the job transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state.</p>"""
    created_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the consumable resource was created.</p>"""
    consumable_resource_properties: NotRequired[
        "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByConsumableResourceSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_queue_arn" in value:
        out["jobQueueArn"] = value["job_queue_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_definition_arn" in value:
        out["jobDefinitionArn"] = value["job_definition_arn"]
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "job_status" in value:
        out["jobStatus"] = value["job_status"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "consumable_resource_properties" in value:
        import capo_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            capo_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListJobsByConsumableResourceSummary:
    out: ListJobsByConsumableResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    if data.get("jobQueueArn") is not None:
        out["job_queue_arn"] = data["jobQueueArn"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("jobDefinitionArn") is not None:
        out["job_definition_arn"] = data["jobDefinitionArn"]
    if data.get("shareIdentifier") is not None:
        out["share_identifier"] = data["shareIdentifier"]
    if data.get("jobStatus") is not None:
        out["job_status"] = data["jobStatus"]
    if data.get("quantity") is not None:
        out["quantity"] = data["quantity"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("startedAt") is not None:
        out["started_at"] = data["startedAt"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("consumableResourceProperties") is not None:
        import capo_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            capo_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
