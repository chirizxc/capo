"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteSecurityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.resource_id_string


class DeleteSecurityConfigurationResponse(TypedDict, closed=True):
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the deleted security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSecurityConfigurationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteSecurityConfigurationResponse:
    out: DeleteSecurityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
