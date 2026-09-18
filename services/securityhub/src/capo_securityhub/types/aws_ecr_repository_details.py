"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcrRepositoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecr_repository_image_scanning_configuration_details
    import capo_securityhub.types.aws_ecr_repository_lifecycle_policy_details
    import capo_securityhub.types.non_empty_string


class AwsEcrRepositoryDetails(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the repository.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_securityhub.types.aws_ecr_repository_image_scanning_configuration_details.AwsEcrRepositoryImageScanningConfigurationDetails"
    ]
    """<p>The image scanning configuration for a repository.</p>"""
    image_tag_mutability: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The tag mutability setting for the repository. Valid values are <code>IMMUTABLE</code> or <code>MUTABLE</code>.</p>"""
    lifecycle_policy: NotRequired[
        "capo_securityhub.types.aws_ecr_repository_lifecycle_policy_details.AwsEcrRepositoryLifecyclePolicyDetails"
    ]
    """<p>Information about the lifecycle policy for the repository.</p>"""
    repository_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the repository.</p>"""
    repository_policy_text: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The text of the repository policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrRepositoryDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "image_scanning_configuration" in value:
        import capo_securityhub.types.aws_ecr_repository_image_scanning_configuration_details

        out["ImageScanningConfiguration"] = (
            capo_securityhub.types.aws_ecr_repository_image_scanning_configuration_details.serialize_json(
                value["image_scanning_configuration"]
            )
        )
    if "image_tag_mutability" in value:
        out["ImageTagMutability"] = value["image_tag_mutability"]
    if "lifecycle_policy" in value:
        import capo_securityhub.types.aws_ecr_repository_lifecycle_policy_details

        out["LifecyclePolicy"] = (
            capo_securityhub.types.aws_ecr_repository_lifecycle_policy_details.serialize_json(
                value["lifecycle_policy"]
            )
        )
    if "repository_name" in value:
        out["RepositoryName"] = value["repository_name"]
    if "repository_policy_text" in value:
        out["RepositoryPolicyText"] = value["repository_policy_text"]
    return out


def deserialize_json(data: dict) -> AwsEcrRepositoryDetails:
    out: AwsEcrRepositoryDetails = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ImageScanningConfiguration") is not None:
        import capo_securityhub.types.aws_ecr_repository_image_scanning_configuration_details

        out["image_scanning_configuration"] = (
            capo_securityhub.types.aws_ecr_repository_image_scanning_configuration_details.deserialize_json(
                data["ImageScanningConfiguration"]
            )
        )
    if data.get("ImageTagMutability") is not None:
        out["image_tag_mutability"] = data["ImageTagMutability"]
    if data.get("LifecyclePolicy") is not None:
        import capo_securityhub.types.aws_ecr_repository_lifecycle_policy_details

        out["lifecycle_policy"] = (
            capo_securityhub.types.aws_ecr_repository_lifecycle_policy_details.deserialize_json(
                data["LifecyclePolicy"]
            )
        )
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    if data.get("RepositoryPolicyText") is not None:
        out["repository_policy_text"] = data["RepositoryPolicyText"]
    return out
