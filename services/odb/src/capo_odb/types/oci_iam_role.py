"""Generated from Smithy shape ``com.amazonaws.odb#OciIamRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.oci_aws_integration
    import capo_odb.types.oci_iam_role_status
    import capo_odb.types.role_arn


class OciIamRole(TypedDict, closed=True):
    iam_role_arn: NotRequired["capo_odb.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""
    aws_integration: NotRequired["capo_odb.types.oci_aws_integration.OciAwsIntegration"]
    """<p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""
    status: NotRequired["capo_odb.types.oci_iam_role_status.OciIamRoleStatus"]
    """<p>The current lifecycle status of the IAM service role.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the IAM service role, if applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciIamRole) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "aws_integration" in value:
        import capo_odb.types.oci_aws_integration

        out["awsIntegration"] = (
            capo_odb.types.oci_aws_integration.serialize_aws_json_1_0(
                value["aws_integration"]
            )
        )
    if "status" in value:
        import capo_odb.types.oci_iam_role_status

        out["status"] = capo_odb.types.oci_iam_role_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OciIamRole:
    out: OciIamRole = {}  # type: ignore[typeddict-item]
    if data.get("iamRoleArn") is not None:
        out["iam_role_arn"] = data["iamRoleArn"]
    if data.get("awsIntegration") is not None:
        import capo_odb.types.oci_aws_integration

        out["aws_integration"] = (
            capo_odb.types.oci_aws_integration.deserialize_aws_json_1_0(
                data["awsIntegration"]
            )
        )
    if data.get("status") is not None:
        import capo_odb.types.oci_iam_role_status

        out["status"] = capo_odb.types.oci_iam_role_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
