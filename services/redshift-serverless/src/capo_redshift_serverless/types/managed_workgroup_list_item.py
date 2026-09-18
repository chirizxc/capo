"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ManagedWorkgroupListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.managed_workgroup_name
    import capo_redshift_serverless.types.managed_workgroup_status
    import capo_redshift_serverless.types.source_arn


class ManagedWorkgroupListItem(TypedDict, closed=True):
    managed_workgroup_name: NotRequired[
        "capo_redshift_serverless.types.managed_workgroup_name.ManagedWorkgroupName"
    ]
    """<p>The name of the managed workgroup.</p>"""
    managed_workgroup_id: NotRequired["str"]
    """<p>The unique identifier of the managed workgroup.</p>"""
    source_arn: NotRequired["capo_redshift_serverless.types.source_arn.SourceArn"]
    """<p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>"""
    status: NotRequired[
        "capo_redshift_serverless.types.managed_workgroup_status.ManagedWorkgroupStatus"
    ]
    """<p>The status of the managed workgroup.</p>"""
    creation_date: NotRequired["datetime.datetime"]
    """<p>The creation date of the managed workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedWorkgroupListItem) -> dict:
    out: dict = {}
    if "managed_workgroup_name" in value:
        out["managedWorkgroupName"] = value["managed_workgroup_name"]
    if "managed_workgroup_id" in value:
        out["managedWorkgroupId"] = value["managed_workgroup_id"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    if "status" in value:
        import capo_redshift_serverless.types.managed_workgroup_status

        out["status"] = (
            capo_redshift_serverless.types.managed_workgroup_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_date" in value:
        import capo_redshift_serverless._protocol.serialize

        out["creationDate"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["creation_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedWorkgroupListItem:
    out: ManagedWorkgroupListItem = {}  # type: ignore[typeddict-item]
    if data.get("managedWorkgroupName") is not None:
        out["managed_workgroup_name"] = data["managedWorkgroupName"]
    if data.get("managedWorkgroupId") is not None:
        out["managed_workgroup_id"] = data["managedWorkgroupId"]
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    if data.get("status") is not None:
        import capo_redshift_serverless.types.managed_workgroup_status

        out["status"] = (
            capo_redshift_serverless.types.managed_workgroup_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("creationDate") is not None:
        import datetime

        out["creation_date"] = datetime.datetime.fromisoformat(
            data["creationDate"].replace("Z", "+00:00")
        )
    return out
