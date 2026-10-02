"""Generated from Smithy shape ``com.amazonaws.emrcontainers#IAMConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.iam_role_arn


class IAMConfiguration(TypedDict, closed=True):
    system_role: NotRequired["capo_emr_containers.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the system role used by the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMConfiguration) -> dict:
    out: dict = {}
    if "system_role" in value:
        out["systemRole"] = value["system_role"]
    return out


def deserialize_json(data: dict) -> IAMConfiguration:
    out: IAMConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("systemRole") is not None:
        out["system_role"] = data["systemRole"]
    return out
