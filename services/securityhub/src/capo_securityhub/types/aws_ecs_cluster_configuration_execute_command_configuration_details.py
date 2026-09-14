"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterConfigurationExecuteCommandConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details
    import capo_securityhub.types.non_empty_string


class AwsEcsClusterConfigurationExecuteCommandConfigurationDetails(
    TypedDict, closed=True
):
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the KMS key that is used to encrypt the data between the local client and the container.</p>"""
    log_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details.AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails"
    ]
    """<p>The log configuration for the results of the run command actions. Required if <code>Logging</code> is <code>NONE</code>.</p>"""
    logging: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The log setting to use for redirecting logs for run command results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsClusterConfigurationExecuteCommandConfigurationDetails,
) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "log_configuration" in value:
        import capo_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details

        out["LogConfiguration"] = (
            capo_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details.serialize_json(
                value["log_configuration"]
            )
        )
    if "logging" in value:
        out["Logging"] = value["logging"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsClusterConfigurationExecuteCommandConfigurationDetails:
    out: AwsEcsClusterConfigurationExecuteCommandConfigurationDetails = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("LogConfiguration") is not None:
        import capo_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details

        out["log_configuration"] = (
            capo_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details.deserialize_json(
                data["LogConfiguration"]
            )
        )
    if data.get("Logging") is not None:
        out["logging"] = data["Logging"]
    return out
