"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExecutionSummaryAffectedSession``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class ExecutionSummaryAffectedSession(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the session.</p>"""
    approach_taken: "str"
    """<p>The approach taken by the agent during this session.</p>"""
    final_outcome: "str"
    """<p>The final outcome of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaryAffectedSession) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["approachTaken"] = value["approach_taken"]
    out["finalOutcome"] = value["final_outcome"]
    return out


def deserialize_json(data: dict) -> ExecutionSummaryAffectedSession:
    out: ExecutionSummaryAffectedSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError(
            "ExecutionSummaryAffectedSession.session_id required"
        )
    if data.get("approachTaken") is not None:
        out["approach_taken"] = data["approachTaken"]
    else:
        raise DeserializationError(
            "ExecutionSummaryAffectedSession.approach_taken required"
        )
    if data.get("finalOutcome") is not None:
        out["final_outcome"] = data["finalOutcome"]
    else:
        raise DeserializationError(
            "ExecutionSummaryAffectedSession.final_outcome required"
        )
    return out
