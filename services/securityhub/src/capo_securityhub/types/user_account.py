"""Generated from Smithy shape ``com.amazonaws.securityhub#UserAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class UserAccount(TypedDict, closed=True):
    uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The unique identifier of the user account involved in the attack sequence. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the user account involved in the attack sequence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccount) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UserAccount:
    out: UserAccount = {}  # type: ignore[typeddict-item]
    if data.get("Uid") is not None:
        out["uid"] = data["Uid"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
