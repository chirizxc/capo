"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcrRepositoryLifecyclePolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEcrRepositoryLifecyclePolicyDetails(TypedDict, closed=True):
    lifecycle_policy_text: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The text of the lifecycle policy.</p>"""
    registry_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account identifier that is associated with the registry that contains the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrRepositoryLifecyclePolicyDetails) -> dict:
    out: dict = {}
    if "lifecycle_policy_text" in value:
        out["LifecyclePolicyText"] = value["lifecycle_policy_text"]
    if "registry_id" in value:
        out["RegistryId"] = value["registry_id"]
    return out


def deserialize_json(data: dict) -> AwsEcrRepositoryLifecyclePolicyDetails:
    out: AwsEcrRepositoryLifecyclePolicyDetails = {}  # type: ignore[typeddict-item]
    if data.get("LifecyclePolicyText") is not None:
        out["lifecycle_policy_text"] = data["LifecyclePolicyText"]
    if data.get("RegistryId") is not None:
        out["registry_id"] = data["RegistryId"]
    return out
