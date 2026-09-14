"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDeployedStackDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.logical_id
    import capo_mgn.types.network_migration_deployed_stack_status
    import capo_mgn.types.network_migration_failed_resources_list
    import capo_mgn.types.physical_id
    import capo_mgn.types.segment_id


class NetworkMigrationDeployedStackDetails(TypedDict, closed=True):
    status: NotRequired[
        "capo_mgn.types.network_migration_deployed_stack_status.NetworkMigrationDeployedStackStatus"
    ]
    """<p>The current status of the deployed stack.</p>"""
    stack_physical_id: NotRequired["capo_mgn.types.physical_id.PhysicalID"]
    """<p>The physical ID of the CloudFormation stack.</p>"""
    stack_logical_id: NotRequired["capo_mgn.types.logical_id.LogicalID"]
    """<p>The logical ID of the stack.</p>"""
    segment_id: NotRequired["capo_mgn.types.segment_id.SegmentID"]
    """<p>The ID of the segment that this stack was deployed for.</p>"""
    target_account: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The target AWS account where the stack was deployed.</p>"""
    failed_resources: NotRequired[
        "capo_mgn.types.network_migration_failed_resources_list.NetworkMigrationFailedResourcesList"
    ]
    """<p>A list of resources that failed to deploy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDeployedStackDetails) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "stack_physical_id" in value:
        out["stackPhysicalID"] = value["stack_physical_id"]
    if "stack_logical_id" in value:
        out["stackLogicalID"] = value["stack_logical_id"]
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "failed_resources" in value:
        import capo_mgn.types.network_migration_failed_resources_list

        out["failedResources"] = (
            capo_mgn.types.network_migration_failed_resources_list.serialize_json(
                value["failed_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationDeployedStackDetails:
    out: NetworkMigrationDeployedStackDetails = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("stackPhysicalID") is not None:
        out["stack_physical_id"] = data["stackPhysicalID"]
    if data.get("stackLogicalID") is not None:
        out["stack_logical_id"] = data["stackLogicalID"]
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    if data.get("targetAccount") is not None:
        out["target_account"] = data["targetAccount"]
    if data.get("failedResources") is not None:
        import capo_mgn.types.network_migration_failed_resources_list

        out["failed_resources"] = (
            capo_mgn.types.network_migration_failed_resources_list.deserialize_json(
                data["failedResources"]
            )
        )
    return out
