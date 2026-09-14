"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.account_id
    import capo_codecommit.types.arn
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.clone_url_http
    import capo_codecommit.types.clone_url_ssh
    import capo_codecommit.types.creation_date
    import capo_codecommit.types.kms_key_id
    import capo_codecommit.types.last_modified_date
    import capo_codecommit.types.repository_description
    import capo_codecommit.types.repository_id
    import capo_codecommit.types.repository_name


class RepositoryMetadata(TypedDict, closed=True):
    account_id: NotRequired["capo_codecommit.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the repository.</p>"""
    repository_id: NotRequired["capo_codecommit.types.repository_id.RepositoryId"]
    """<p>The ID of the repository.</p>"""
    repository_name: NotRequired["capo_codecommit.types.repository_name.RepositoryName"]
    """<p>The repository's name.</p>"""
    repository_description: NotRequired[
        "capo_codecommit.types.repository_description.RepositoryDescription"
    ]
    """<p>A comment or description about the repository.</p>"""
    default_branch: NotRequired["capo_codecommit.types.branch_name.BranchName"]
    """<p>The repository's default branch name.</p>"""
    last_modified_date: NotRequired[
        "capo_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date and time the repository was last modified, in timestamp format.</p>"""
    creation_date: NotRequired["capo_codecommit.types.creation_date.CreationDate"]
    """<p>The date and time the repository was created, in timestamp format.</p>"""
    clone_url_http: NotRequired["capo_codecommit.types.clone_url_http.CloneUrlHttp"]
    """<p>The URL to use for cloning the repository over HTTPS.</p>"""
    clone_url_ssh: NotRequired["capo_codecommit.types.clone_url_ssh.CloneUrlSsh"]
    """<p>The URL to use for cloning the repository over SSH.</p>"""
    arn: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the repository.</p>"""
    kms_key_id: NotRequired["capo_codecommit.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service encryption key used to encrypt and decrypt the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryMetadata) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "repository_description" in value:
        out["repositoryDescription"] = value["repository_description"]
    if "default_branch" in value:
        out["defaultBranch"] = value["default_branch"]
    if "last_modified_date" in value:
        import capo_codecommit.types.last_modified_date

        out["lastModifiedDate"] = (
            capo_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_codecommit.types.creation_date

        out["creationDate"] = (
            capo_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "clone_url_http" in value:
        out["cloneUrlHttp"] = value["clone_url_http"]
    if "clone_url_ssh" in value:
        out["cloneUrlSsh"] = value["clone_url_ssh"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryMetadata:
    out: RepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("repositoryId") is not None:
        out["repository_id"] = data["repositoryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("repositoryDescription") is not None:
        out["repository_description"] = data["repositoryDescription"]
    if data.get("defaultBranch") is not None:
        out["default_branch"] = data["defaultBranch"]
    if data.get("lastModifiedDate") is not None:
        import capo_codecommit.types.last_modified_date

        out["last_modified_date"] = (
            capo_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
                data["lastModifiedDate"]
            )
        )
    if data.get("creationDate") is not None:
        import capo_codecommit.types.creation_date

        out["creation_date"] = (
            capo_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if data.get("cloneUrlHttp") is not None:
        out["clone_url_http"] = data["cloneUrlHttp"]
    if data.get("cloneUrlSsh") is not None:
        out["clone_url_ssh"] = data["cloneUrlSsh"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
