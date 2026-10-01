"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteSecurityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.resource_id_string


class DeleteSecurityConfigurationRequest(TypedDict, closed=True):
    id: "capo_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the security configuration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSecurityConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSecurityConfigurationRequest:
    out: DeleteSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
