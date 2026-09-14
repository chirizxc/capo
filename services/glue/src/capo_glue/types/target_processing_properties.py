"""Generated from Smithy shape ``com.amazonaws.glue#TargetProcessingProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.string128
    import capo_glue.types.string2048


class TargetProcessingProperties(TypedDict, closed=True):
    role_arn: NotRequired["capo_glue.types.string128.String128"]
    """<p>The IAM role to access the Glue database.</p>"""
    kms_arn: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>The ARN of the KMS key used for encryption.</p>"""
    connection_name: NotRequired["capo_glue.types.string128.String128"]
    """<p>The Glue network connection to configure the Glue job running in the customer VPC.</p>"""
    event_bus_arn: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>The ARN of an Eventbridge event bus to receive the integration status notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetProcessingProperties) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "kms_arn" in value:
        out["KmsArn"] = value["kms_arn"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetProcessingProperties:
    out: TargetProcessingProperties = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("KmsArn") is not None:
        out["kms_arn"] = data["KmsArn"]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    return out
