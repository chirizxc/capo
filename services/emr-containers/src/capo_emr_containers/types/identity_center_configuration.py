"""Generated from Smithy shape ``com.amazonaws.emrcontainers#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.boolean
    import capo_emr_containers.types.emr_identity_center_application_arn
    import capo_emr_containers.types.identity_center_instance_arn


class IdentityCenterConfiguration(TypedDict, closed=True):
    enable_identity_center: NotRequired["capo_emr_containers.types.boolean.Boolean"]
    """<p>Specifies whether Identity Center is enabled for the security configuration.</p>"""
    identity_center_application_assignment_required: NotRequired[
        "capo_emr_containers.types.boolean.Boolean"
    ]
    """<p>Specifies whether user assignment is required for the Identity Center application.</p>"""
    identity_center_instance_arn: NotRequired[
        "capo_emr_containers.types.identity_center_instance_arn.IdentityCenterInstanceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Identity Center instance.</p>"""
    emr_identity_center_application_arn: NotRequired[
        "capo_emr_containers.types.emr_identity_center_application_arn.EmrIdentityCenterApplicationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon EMR Identity Center application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    if "enable_identity_center" in value:
        out["enableIdentityCenter"] = value["enable_identity_center"]
    if "identity_center_application_assignment_required" in value:
        out["identityCenterApplicationAssignmentRequired"] = value[
            "identity_center_application_assignment_required"
        ]
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceARN"] = value["identity_center_instance_arn"]
    if "emr_identity_center_application_arn" in value:
        out["emrIdentityCenterApplicationARN"] = value[
            "emr_identity_center_application_arn"
        ]
    return out


def deserialize_json(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enableIdentityCenter") is not None:
        out["enable_identity_center"] = data["enableIdentityCenter"]
    if data.get("identityCenterApplicationAssignmentRequired") is not None:
        out["identity_center_application_assignment_required"] = data[
            "identityCenterApplicationAssignmentRequired"
        ]
    if data.get("identityCenterInstanceARN") is not None:
        out["identity_center_instance_arn"] = data["identityCenterInstanceARN"]
    if data.get("emrIdentityCenterApplicationARN") is not None:
        out["emr_identity_center_application_arn"] = data[
            "emrIdentityCenterApplicationARN"
        ]
    return out
