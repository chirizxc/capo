"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AffectedSession``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_span_detail_list


class AffectedSession(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the affected session.</p>"""
    explanation: "str"
    """<p>An explanation of how the failure manifested in this session.</p>"""
    fix_type: "str"
    """<p>The type of fix recommended for this failure.</p>"""
    recommendation: "str"
    """<p>The specific fix recommendation for this session.</p>"""
    failure_spans: (
        "capo_bedrock_agentcore.types.failure_span_detail_list.FailureSpanDetailList"
    )
    """<p>The list of spans where failures were detected in this session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AffectedSession) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["explanation"] = value["explanation"]
    out["fixType"] = value["fix_type"]
    out["recommendation"] = value["recommendation"]
    import capo_bedrock_agentcore.types.failure_span_detail_list

    out["failureSpans"] = (
        capo_bedrock_agentcore.types.failure_span_detail_list.serialize_json(
            value["failure_spans"]
        )
    )
    return out


def deserialize_json(data: dict) -> AffectedSession:
    out: AffectedSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("AffectedSession.session_id required")
    if data.get("explanation") is not None:
        out["explanation"] = data["explanation"]
    else:
        raise DeserializationError("AffectedSession.explanation required")
    if data.get("fixType") is not None:
        out["fix_type"] = data["fixType"]
    else:
        raise DeserializationError("AffectedSession.fix_type required")
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    else:
        raise DeserializationError("AffectedSession.recommendation required")
    if data.get("failureSpans") is not None:
        import capo_bedrock_agentcore.types.failure_span_detail_list

        out["failure_spans"] = (
            capo_bedrock_agentcore.types.failure_span_detail_list.deserialize_json(
                data["failureSpans"]
            )
        )
    else:
        raise DeserializationError("AffectedSession.failure_spans required")
    return out
