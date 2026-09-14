"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSecretsManagerSecretDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_secrets_manager_secret_rotation_rules
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsSecretsManagerSecretDetails(TypedDict, closed=True):
    rotation_rules: NotRequired[
        "capo_securityhub.types.aws_secrets_manager_secret_rotation_rules.AwsSecretsManagerSecretRotationRules"
    ]
    """<p>Defines the rotation schedule for the secret.</p>"""
    rotation_occurred_within_frequency: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether the rotation occurred within the specified rotation frequency.</p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN, Key ID, or alias of the KMS key used to encrypt the <code>SecretString</code> or <code>SecretBinary</code> values for versions of this secret.</p>"""
    rotation_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether rotation is enabled.</p>"""
    rotation_lambda_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Lambda function that rotates the secret.</p>"""
    deleted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the secret is deleted.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the secret.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The user-provided description of the secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSecretsManagerSecretDetails) -> dict:
    out: dict = {}
    if "rotation_rules" in value:
        import capo_securityhub.types.aws_secrets_manager_secret_rotation_rules

        out["RotationRules"] = (
            capo_securityhub.types.aws_secrets_manager_secret_rotation_rules.serialize_json(
                value["rotation_rules"]
            )
        )
    if "rotation_occurred_within_frequency" in value:
        out["RotationOccurredWithinFrequency"] = value[
            "rotation_occurred_within_frequency"
        ]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "rotation_enabled" in value:
        out["RotationEnabled"] = value["rotation_enabled"]
    if "rotation_lambda_arn" in value:
        out["RotationLambdaArn"] = value["rotation_lambda_arn"]
    if "deleted" in value:
        out["Deleted"] = value["deleted"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AwsSecretsManagerSecretDetails:
    out: AwsSecretsManagerSecretDetails = {}  # type: ignore[typeddict-item]
    if data.get("RotationRules") is not None:
        import capo_securityhub.types.aws_secrets_manager_secret_rotation_rules

        out["rotation_rules"] = (
            capo_securityhub.types.aws_secrets_manager_secret_rotation_rules.deserialize_json(
                data["RotationRules"]
            )
        )
    if data.get("RotationOccurredWithinFrequency") is not None:
        out["rotation_occurred_within_frequency"] = data[
            "RotationOccurredWithinFrequency"
        ]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("RotationEnabled") is not None:
        out["rotation_enabled"] = data["RotationEnabled"]
    if data.get("RotationLambdaArn") is not None:
        out["rotation_lambda_arn"] = data["RotationLambdaArn"]
    if data.get("Deleted") is not None:
        out["deleted"] = data["Deleted"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
