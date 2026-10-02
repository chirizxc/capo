"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceOwnerOrg``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ResourceOwnerOrg(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the organization that owns the resource, for example, Azure Tenant Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOwnerOrg) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ResourceOwnerOrg:
    out: ResourceOwnerOrg = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
