"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.description
    import capo_finspace.types.environment_arn
    import capo_finspace.types.environment_status
    import capo_finspace.types.id_type
    import capo_finspace.types.kms_key_id
    import capo_finspace.types.kx_environment_name
    import capo_finspace.types.timestamp


class CreateKxEnvironmentResponse(TypedDict, closed=True):
    name: NotRequired["capo_finspace.types.kx_environment_name.KxEnvironmentName"]
    """<p>The name of the kdb environment.</p>"""
    status: NotRequired["capo_finspace.types.environment_status.EnvironmentStatus"]
    """<p>The status of the kdb environment.</p>"""
    environment_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the kdb environment.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description for the kdb environment.</p>"""
    environment_arn: NotRequired["capo_finspace.types.environment_arn.EnvironmentArn"]
    """<p>The ARN identifier of the environment.</p>"""
    kms_key_id: NotRequired["capo_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key ID to encrypt your data in the FinSpace environment.</p>"""
    creation_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb environment was created in FinSpace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxEnvironmentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_finspace.types.environment_status

        out["status"] = capo_finspace.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "creation_timestamp" in value:
        import capo_finspace.types.timestamp

        out["creationTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> CreateKxEnvironmentResponse:
    out: CreateKxEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_finspace.types.environment_status

        out["status"] = capo_finspace.types.environment_status.deserialize_json(
            data["status"]
        )
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("creationTimestamp") is not None:
        import capo_finspace.types.timestamp

        out["creation_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    return out
