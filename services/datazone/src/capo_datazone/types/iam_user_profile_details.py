"""Generated from Smithy shape ``com.amazonaws.datazone#IamUserProfileDetails``."""

from typing_extensions import NotRequired, TypedDict


class IamUserProfileDetails(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The ARN of the IAM user.</p>"""
    principal_id: NotRequired["str"]
    """<p>The principal ID as part of the IAM user profile details.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""
    group_profile_id: NotRequired["str"]
    """<p>The identifier of the group profile associated with the IAM user profile. This links the user to a specific group profile within the Amazon DataZone domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamUserProfileDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "group_profile_id" in value:
        out["groupProfileId"] = value["group_profile_id"]
    return out


def deserialize_json(data: dict) -> IamUserProfileDetails:
    out: IamUserProfileDetails = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    if data.get("groupProfileId") is not None:
        out["group_profile_id"] = data["groupProfileId"]
    return out
