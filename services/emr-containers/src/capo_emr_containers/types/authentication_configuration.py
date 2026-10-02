"""Generated from Smithy shape ``com.amazonaws.emrcontainers#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.iam_configuration
    import capo_emr_containers.types.identity_center_configuration


class AuthenticationConfiguration(TypedDict, closed=True):
    identity_center_configuration: NotRequired[
        "capo_emr_containers.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p>The IAM Identity Center configuration to use for authentication.</p>"""
    iam_configuration: NotRequired[
        "capo_emr_containers.types.iam_configuration.IAMConfiguration"
    ]
    """<p>The IAM configuration to use for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    if "identity_center_configuration" in value:
        import capo_emr_containers.types.identity_center_configuration

        out["identityCenterConfiguration"] = (
            capo_emr_containers.types.identity_center_configuration.serialize_json(
                value["identity_center_configuration"]
            )
        )
    if "iam_configuration" in value:
        import capo_emr_containers.types.iam_configuration

        out["iamConfiguration"] = (
            capo_emr_containers.types.iam_configuration.serialize_json(
                value["iam_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("identityCenterConfiguration") is not None:
        import capo_emr_containers.types.identity_center_configuration

        out["identity_center_configuration"] = (
            capo_emr_containers.types.identity_center_configuration.deserialize_json(
                data["identityCenterConfiguration"]
            )
        )
    if data.get("iamConfiguration") is not None:
        import capo_emr_containers.types.iam_configuration

        out["iam_configuration"] = (
            capo_emr_containers.types.iam_configuration.deserialize_json(
                data["iamConfiguration"]
            )
        )
    return out
