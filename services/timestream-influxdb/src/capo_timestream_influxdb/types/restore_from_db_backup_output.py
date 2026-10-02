"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RestoreFromDbBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.engine_type
    import capo_timestream_influxdb.types.resource_deployment_type
    import capo_timestream_influxdb.types.resource_type
    import capo_timestream_influxdb.types.restore_status


class RestoreFromDbBackupOutput(TypedDict, closed=True):
    restored_db_resource_id: NotRequired[
        "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
    ]
    """<p>The identifier of the restored DB resource.</p>"""
    restore_status: NotRequired[
        "capo_timestream_influxdb.types.restore_status.RestoreStatus"
    ]
    """<p>The status of the restore operation.</p>"""
    resource_type: NotRequired[
        "capo_timestream_influxdb.types.resource_type.ResourceType"
    ]
    """<p>The type of the restored resource. Valid values are DB_INSTANCE and DB_CLUSTER.</p>"""
    engine_type: NotRequired["capo_timestream_influxdb.types.engine_type.EngineType"]
    """<p>The engine type of the restored resource.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
    ]
    """<p>The deployment type of the restored resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreFromDbBackupOutput) -> dict:
    out: dict = {}
    if "restored_db_resource_id" in value:
        out["restoredDbResourceId"] = value["restored_db_resource_id"]
    if "restore_status" in value:
        import capo_timestream_influxdb.types.restore_status

        out["restoreStatus"] = (
            capo_timestream_influxdb.types.restore_status.serialize_aws_json_1_0(
                value["restore_status"]
            )
        )
    if "resource_type" in value:
        import capo_timestream_influxdb.types.resource_type

        out["resourceType"] = (
            capo_timestream_influxdb.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "engine_type" in value:
        import capo_timestream_influxdb.types.engine_type

        out["engineType"] = (
            capo_timestream_influxdb.types.engine_type.serialize_aws_json_1_0(
                value["engine_type"]
            )
        )
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.resource_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreFromDbBackupOutput:
    out: RestoreFromDbBackupOutput = {}  # type: ignore[typeddict-item]
    if data.get("restoredDbResourceId") is not None:
        out["restored_db_resource_id"] = data["restoredDbResourceId"]
    if data.get("restoreStatus") is not None:
        import capo_timestream_influxdb.types.restore_status

        out["restore_status"] = (
            capo_timestream_influxdb.types.restore_status.deserialize_aws_json_1_0(
                data["restoreStatus"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_timestream_influxdb.types.resource_type

        out["resource_type"] = (
            capo_timestream_influxdb.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if data.get("engineType") is not None:
        import capo_timestream_influxdb.types.engine_type

        out["engine_type"] = (
            capo_timestream_influxdb.types.engine_type.deserialize_aws_json_1_0(
                data["engineType"]
            )
        )
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.resource_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    return out
