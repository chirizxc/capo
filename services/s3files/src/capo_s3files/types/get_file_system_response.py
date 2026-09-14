"""Generated from Smithy shape ``com.amazonaws.s3files#GetFileSystemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3files.types.aws_account_id
    import capo_s3files.types.bucket_arn
    import capo_s3files.types.client_token
    import capo_s3files.types.file_system_arn
    import capo_s3files.types.file_system_id
    import capo_s3files.types.kms_key_id
    import capo_s3files.types.life_cycle_state
    import capo_s3files.types.role_arn
    import capo_s3files.types.status_message
    import capo_s3files.types.tag_list
    import capo_s3files.types.tag_value


class GetFileSystemResponse(TypedDict, closed=True):
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time when the file system was created.</p>"""
    file_system_arn: NotRequired["capo_s3files.types.file_system_arn.FileSystemArn"]
    """<p>The Amazon Resource Name (ARN) of the file system.</p>"""
    file_system_id: NotRequired["capo_s3files.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system.</p>"""
    bucket: NotRequired["capo_s3files.types.bucket_arn.BucketArn"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    prefix: "str"
    """<p>The prefix in the S3 bucket that the file system provides access to.</p>"""
    client_token: NotRequired["capo_s3files.types.client_token.ClientToken"]
    """<p>The client token used for idempotency when the file system was created.</p>"""
    kms_key_id: NotRequired["capo_s3files.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key used for encryption.</p>"""
    status: NotRequired["capo_s3files.types.life_cycle_state.LifeCycleState"]
    """<p>The current status of the file system.</p>"""
    status_message: NotRequired["capo_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the file system status.</p>"""
    role_arn: NotRequired["capo_s3files.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used for S3 access.</p>"""
    owner_id: NotRequired["capo_s3files.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID of the file system owner.</p>"""
    tags: NotRequired["capo_s3files.types.tag_list.TagList"]
    """<p>The tags associated with the file system.</p>"""
    name: NotRequired["capo_s3files.types.tag_value.TagValue"]
    """<p>The name of the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFileSystemResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_s3files.types._prelude.timestamp

        out["creationTime"] = capo_s3files.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "file_system_arn" in value:
        out["fileSystemArn"] = value["file_system_arn"]
    if "file_system_id" in value:
        out["fileSystemId"] = value["file_system_id"]
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    out["prefix"] = value.get("prefix", "")
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "status" in value:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "owner_id" in value:
        out["ownerId"] = value["owner_id"]
    if "tags" in value:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.serialize_json(value["tags"])
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetFileSystemResponse:
    out: GetFileSystemResponse = {}  # type: ignore[typeddict-item]
    if data.get("creationTime") is not None:
        import capo_s3files.types._prelude.timestamp

        out["creation_time"] = capo_s3files.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("fileSystemArn") is not None:
        out["file_system_arn"] = data["fileSystemArn"]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("status") is not None:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    if data.get("tags") is not None:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.deserialize_json(data["tags"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
