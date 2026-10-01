"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.identity_center_instance_arn


class IdentityCenterConfiguration(TypedDict, closed=True):
    identity_center_instance_arn: NotRequired[
        "capo_cloudwatchomni.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """Identity Center instance ARN"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    return out


def deserialize_cbor(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("identityCenterInstanceArn") is not None:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    return out
