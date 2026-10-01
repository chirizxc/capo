"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchFilterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_string_list
    import capo_bedrock_agentcore.types.session_filter_config
    import capo_bedrock_agentcore.types.session_trace_ids_list


class CloudWatchFilterConfig(TypedDict, closed=True):
    session_ids: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_string_list.EvaluationStringList"
    ]
    """<p>A list of specific session IDs to evaluate. If specified, only these sessions are included in the evaluation.</p>"""
    time_range: NotRequired[
        "capo_bedrock_agentcore.types.session_filter_config.SessionFilterConfig"
    ]
    """<p>The time range filter for selecting sessions to evaluate.</p>"""
    session_trace_ids: NotRequired[
        "capo_bedrock_agentcore.types.session_trace_ids_list.SessionTraceIdsList"
    ]
    """<p>A list of session and trace ID pairs that restrict evaluation to specific traces within a session. If specified, only the listed traces are evaluated instead of the entire session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchFilterConfig) -> dict:
    out: dict = {}
    if "session_ids" in value:
        import capo_bedrock_agentcore.types.evaluation_string_list

        out["sessionIds"] = (
            capo_bedrock_agentcore.types.evaluation_string_list.serialize_json(
                value["session_ids"]
            )
        )
    if "time_range" in value:
        import capo_bedrock_agentcore.types.session_filter_config

        out["timeRange"] = (
            capo_bedrock_agentcore.types.session_filter_config.serialize_json(
                value["time_range"]
            )
        )
    if "session_trace_ids" in value:
        import capo_bedrock_agentcore.types.session_trace_ids_list

        out["sessionTraceIds"] = (
            capo_bedrock_agentcore.types.session_trace_ids_list.serialize_json(
                value["session_trace_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchFilterConfig:
    out: CloudWatchFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("sessionIds") is not None:
        import capo_bedrock_agentcore.types.evaluation_string_list

        out["session_ids"] = (
            capo_bedrock_agentcore.types.evaluation_string_list.deserialize_json(
                data["sessionIds"]
            )
        )
    if data.get("timeRange") is not None:
        import capo_bedrock_agentcore.types.session_filter_config

        out["time_range"] = (
            capo_bedrock_agentcore.types.session_filter_config.deserialize_json(
                data["timeRange"]
            )
        )
    if data.get("sessionTraceIds") is not None:
        import capo_bedrock_agentcore.types.session_trace_ids_list

        out["session_trace_ids"] = (
            capo_bedrock_agentcore.types.session_trace_ids_list.deserialize_json(
                data["sessionTraceIds"]
            )
        )
    return out
