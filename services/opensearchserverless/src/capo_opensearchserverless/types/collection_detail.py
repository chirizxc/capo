"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.collection_name
    import capo_opensearchserverless.types.collection_status
    import capo_opensearchserverless.types.collection_type
    import capo_opensearchserverless.types.deletion_protection
    import capo_opensearchserverless.types.fips_endpoints
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.vector_options


class CollectionDetail(TypedDict, closed=True):
    id: NotRequired["capo_opensearchserverless.types.collection_id.CollectionId"]
    """<p>A unique identifier for the collection.</p>"""
    name: NotRequired["capo_opensearchserverless.types.collection_name.CollectionName"]
    """<p>The name of the collection.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.collection_status.CollectionStatus"
    ]
    """<p>The current status of the collection.</p>"""
    type: NotRequired["capo_opensearchserverless.types.collection_type.CollectionType"]
    """<p>The type of collection.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The ARN of the Amazon Web Services KMS key used to encrypt the collection.</p>"""
    standby_replicas: NotRequired[
        "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
    ]
    """<p>Details about an OpenSearch Serverless collection.</p>"""
    deletion_protection: NotRequired[
        "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether deletion protection is <code>ENABLED</code> or <code>DISABLED</code> for the collection.</p>"""
    vector_options: NotRequired[
        "capo_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the collection was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The date and time when the collection was last modified.</p>"""
    collection_endpoint: NotRequired["str"]
    """<p>Collection-specific endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection.</p>"""
    dashboard_endpoint: NotRequired["str"]
    """<p>Collection-specific endpoint used to access OpenSearch Dashboards.</p>"""
    fips_endpoints: NotRequired[
        "capo_opensearchserverless.types.fips_endpoints.FipsEndpoints"
    ]
    """<p>FIPS-compliant endpoints for the collection. These endpoints use FIPS 140-3 validated cryptographic modules and are required for federal government workloads that must comply with FedRAMP security standards.</p>"""
    failure_code: NotRequired["str"]
    """<p>A failure code associated with the request.</p>"""
    failure_message: NotRequired["str"]
    """<p>A message associated with the failure code.</p>"""
    collection_group_name: NotRequired[
        "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group that contains this collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "standby_replicas" in value:
        out["standbyReplicas"] = value["standby_replicas"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "vector_options" in value:
        import capo_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            capo_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    if "collection_endpoint" in value:
        out["collectionEndpoint"] = value["collection_endpoint"]
    if "dashboard_endpoint" in value:
        out["dashboardEndpoint"] = value["dashboard_endpoint"]
    if "fips_endpoints" in value:
        import capo_opensearchserverless.types.fips_endpoints

        out["fipsEndpoints"] = (
            capo_opensearchserverless.types.fips_endpoints.serialize_aws_json_1_0(
                value["fips_endpoints"]
            )
        )
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "collection_group_name" in value:
        out["collectionGroupName"] = value["collection_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionDetail:
    out: CollectionDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("standbyReplicas") is not None:
        out["standby_replicas"] = data["standbyReplicas"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("vectorOptions") is not None:
        import capo_opensearchserverless.types.vector_options

        out["vector_options"] = (
            capo_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if data.get("createdDate") is not None:
        out["created_date"] = data["createdDate"]
    if data.get("lastModifiedDate") is not None:
        out["last_modified_date"] = data["lastModifiedDate"]
    if data.get("collectionEndpoint") is not None:
        out["collection_endpoint"] = data["collectionEndpoint"]
    if data.get("dashboardEndpoint") is not None:
        out["dashboard_endpoint"] = data["dashboardEndpoint"]
    if data.get("fipsEndpoints") is not None:
        import capo_opensearchserverless.types.fips_endpoints

        out["fips_endpoints"] = (
            capo_opensearchserverless.types.fips_endpoints.deserialize_aws_json_1_0(
                data["fipsEndpoints"]
            )
        )
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("collectionGroupName") is not None:
        out["collection_group_name"] = data["collectionGroupName"]
    return out
