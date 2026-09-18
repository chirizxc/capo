"""Generated from Smithy shape ``com.amazonaws.guardduty#AccessKeyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class AccessKeyDetails(TypedDict, closed=True):
    access_key_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The access key ID of the user.</p>"""
    principal_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The principal ID of the user.</p>"""
    user_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the user.</p>"""
    user_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessKeyDetails) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "user_type" in value:
        out["userType"] = value["user_type"]
    return out


def deserialize_json(data: dict) -> AccessKeyDetails:
    out: AccessKeyDetails = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("userType") is not None:
        out["user_type"] = data["userType"]
    return out
