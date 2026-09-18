"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.group_member_name


class GroupMember(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the group member (user).</p>"""
    member_name: NotRequired["capo_quicksight.types.group_member_name.GroupMemberName"]
    """<p>The name of the group member (user).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupMember) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "member_name" in value:
        out["MemberName"] = value["member_name"]
    return out


def deserialize_json(data: dict) -> GroupMember:
    out: GroupMember = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("MemberName") is not None:
        out["member_name"] = data["MemberName"]
    return out
