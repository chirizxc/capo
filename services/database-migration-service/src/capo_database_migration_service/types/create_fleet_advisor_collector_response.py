"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateFleetAdvisorCollectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class CreateFleetAdvisorCollectorResponse(TypedDict, closed=True):
    collector_referenced_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The unique ID of the new Fleet Advisor collector, for example: <code>22fda70c-40d5-4acf-b233-a495bd8eb7f5</code> </p>"""
    collector_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the new Fleet Advisor collector.</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A summary description of the Fleet Advisor collector.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The IAM role that grants permissions to access the specified Amazon S3 bucket.</p>"""
    s3_bucket_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon S3 bucket that the collector uses to store inventory metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetAdvisorCollectorResponse) -> dict:
    out: dict = {}
    if "collector_referenced_id" in value:
        out["CollectorReferencedId"] = value["collector_referenced_id"]
    if "collector_name" in value:
        out["CollectorName"] = value["collector_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetAdvisorCollectorResponse:
    out: CreateFleetAdvisorCollectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("CollectorReferencedId") is not None:
        out["collector_referenced_id"] = data["CollectorReferencedId"]
    if data.get("CollectorName") is not None:
        out["collector_name"] = data["CollectorName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    return out
