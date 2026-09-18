"""Generated from Smithy shape ``com.amazonaws.securityagent#ExecutionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.context_type


class ExecutionContext(TypedDict, closed=True):
    context_type: NotRequired["capo_securityagent.types.context_type.ContextType"]
    """<p>The type of context. Valid values include ERROR, CLIENT_ERROR, WARNING, and INFO.</p>"""
    context: NotRequired["str"]
    """<p>The context message.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The date and time the context was recorded, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionContext) -> dict:
    out: dict = {}
    if "context_type" in value:
        import capo_securityagent.types.context_type

        out["contextType"] = capo_securityagent.types.context_type.serialize_json(
            value["context_type"]
        )
    if "context" in value:
        out["context"] = value["context"]
    if "timestamp" in value:
        import capo_securityagent._protocol.serialize

        out["timestamp"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ExecutionContext:
    out: ExecutionContext = {}  # type: ignore[typeddict-item]
    if data.get("contextType") is not None:
        import capo_securityagent.types.context_type

        out["context_type"] = capo_securityagent.types.context_type.deserialize_json(
            data["contextType"]
        )
    if data.get("context") is not None:
        out["context"] = data["context"]
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    return out
