"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysisJobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.network_migration_job_id
    import capo_mgn.types.network_migration_job_status


class NetworkMigrationAnalysisJobDetails(TypedDict, closed=True):
    job_id: NotRequired["capo_mgn.types.network_migration_job_id.NetworkMigrationJobID"]
    """<p>The unique identifier of the analysis job.</p>"""
    network_migration_execution_id: NotRequired[
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: NotRequired[
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job completed or failed.</p>"""
    status: NotRequired[
        "capo_mgn.types.network_migration_job_status.NetworkMigrationJobStatus"
    ]
    """<p>The current status of the analysis job.</p>"""
    status_details: NotRequired[
        "capo_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Detailed status information about the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationAnalysisJobDetails) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "ended_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["endedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
    return out


def deserialize_json(data: dict) -> NetworkMigrationAnalysisJobDetails:
    out: NetworkMigrationAnalysisJobDetails = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if data.get("createdAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("endedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["ended_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusDetails") is not None:
        out["status_details"] = data["statusDetails"]
    return out
