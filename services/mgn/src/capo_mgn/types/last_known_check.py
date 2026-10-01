"""Generated from Smithy shape ``com.amazonaws.mgn#LastKnownCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.bounded_string
    import capo_mgn.types.last_known_check_status
    import capo_mgn.types.last_known_check_type


class LastKnownCheck(TypedDict, closed=True):
    type: NotRequired["capo_mgn.types.last_known_check_type.LastKnownCheckType"]
    """<p>Last known check type.</p>"""
    name: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Last known check name.</p>"""
    status: NotRequired["capo_mgn.types.last_known_check_status.LastKnownCheckStatus"]
    """<p>Last known check status.</p>"""
    error: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Last known check error.</p>"""
    checked_at: NotRequired["datetime.datetime"]
    """<p>Last known check timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastKnownCheck) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "error" in value:
        out["error"] = value["error"]
    if "checked_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["checkedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["checked_at"]
        )
    return out


def deserialize_json(data: dict) -> LastKnownCheck:
    out: LastKnownCheck = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("checkedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["checked_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["checkedAt"]
        )
    return out
