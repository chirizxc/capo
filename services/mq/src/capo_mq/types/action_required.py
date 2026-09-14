"""Generated from Smithy shape ``com.amazonaws.mq#ActionRequired``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string


class ActionRequired(TypedDict, closed=True):
    action_required_code: NotRequired["capo_mq.types.__string.__string"]
    """<p>The code you can use to find instructions on the action required to resolve your broker issue.</p>"""
    action_required_info: NotRequired["capo_mq.types.__string.__string"]
    """<p>Information about the action required to resolve your broker issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionRequired) -> dict:
    out: dict = {}
    if "action_required_code" in value:
        out["actionRequiredCode"] = value["action_required_code"]
    if "action_required_info" in value:
        out["actionRequiredInfo"] = value["action_required_info"]
    return out


def deserialize_json(data: dict) -> ActionRequired:
    out: ActionRequired = {}  # type: ignore[typeddict-item]
    if data.get("actionRequiredCode") is not None:
        out["action_required_code"] = data["actionRequiredCode"]
    if data.get("actionRequiredInfo") is not None:
        out["action_required_info"] = data["actionRequiredInfo"]
    return out
