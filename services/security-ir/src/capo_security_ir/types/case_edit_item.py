"""Generated from Smithy shape ``com.amazonaws.securityir#CaseEditItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.case_edit_action
    import capo_security_ir.types.case_edit_message


class CaseEditItem(TypedDict, closed=True):
    event_timestamp: NotRequired["datetime.datetime"]
    """<p/>"""
    principal: NotRequired["str"]
    """<p/>"""
    action: NotRequired["capo_security_ir.types.case_edit_action.CaseEditAction"]
    """<p/>"""
    message: NotRequired["capo_security_ir.types.case_edit_message.CaseEditMessage"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseEditItem) -> dict:
    out: dict = {}
    if "event_timestamp" in value:
        import capo_security_ir.types._prelude.timestamp

        out["eventTimestamp"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["event_timestamp"]
            )
        )
    if "principal" in value:
        out["principal"] = value["principal"]
    if "action" in value:
        out["action"] = value["action"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CaseEditItem:
    out: CaseEditItem = {}  # type: ignore[typeddict-item]
    if data.get("eventTimestamp") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    if data.get("action") is not None:
        out["action"] = data["action"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
