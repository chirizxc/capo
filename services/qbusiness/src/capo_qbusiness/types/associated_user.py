"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatedUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.membership_type
    import capo_qbusiness.types.string


class AssociatedUser(TypedDict, closed=True):
    id: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The unique identifier of the associated user. This is used to identify the user in access control decisions.</p>"""
    type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the associated user. This indicates the scope of the user's association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> AssociatedUser:
    out: AssociatedUser = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
