"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceOwnerAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ResourceOwnerAccount(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the account that owns the resource, for example, Azure Subscription Id or Amazon Web Services Account Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOwnerAccount) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ResourceOwnerAccount:
    out: ResourceOwnerAccount = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
