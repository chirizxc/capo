"""Generated from Smithy shape ``com.amazonaws.odb#CustomerManagedAwsSecretConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.external_id_type
    import capo_odb.types.role_arn
    import capo_odb.types.secret_id_or_arn


class CustomerManagedAwsSecretConfiguration(TypedDict, closed=True):
    iam_role_arn: NotRequired["capo_odb.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that OCI assumes to retrieve the secret value.</p>"""
    secret_id: NotRequired["capo_odb.types.secret_id_or_arn.SecretIdOrArn"]
    """<p>The identifier or ARN of the Amazon Web Services Secrets Manager secret that contains the password.</p>"""
    external_id_type: NotRequired["capo_odb.types.external_id_type.ExternalIdType"]
    """<p>The type of Oracle Cloud Identifier (OCID) used as the external ID when assuming the IAM role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerManagedAwsSecretConfiguration) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "secret_id" in value:
        out["secretId"] = value["secret_id"]
    if "external_id_type" in value:
        import capo_odb.types.external_id_type

        out["externalIdType"] = capo_odb.types.external_id_type.serialize_aws_json_1_0(
            value["external_id_type"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomerManagedAwsSecretConfiguration:
    out: CustomerManagedAwsSecretConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("iamRoleArn") is not None:
        out["iam_role_arn"] = data["iamRoleArn"]
    if data.get("secretId") is not None:
        out["secret_id"] = data["secretId"]
    if data.get("externalIdType") is not None:
        import capo_odb.types.external_id_type

        out["external_id_type"] = (
            capo_odb.types.external_id_type.deserialize_aws_json_1_0(
                data["externalIdType"]
            )
        )
    return out
