"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.log_stream_name
    import capo_bedrock_agentcore.types.metrics_namespace
    import capo_bedrock_agentcore.types.optional_log_group_name
    import capo_bedrock_agentcore.types.result_destination


class CloudWatchOutputConfig(TypedDict, closed=True):
    log_group_name: (
        "capo_bedrock_agentcore.types.optional_log_group_name.OptionalLogGroupName"
    )
    """<p>The name of the CloudWatch log group where evaluation results will be written. This value doesn't apply when <code>resultDestination</code> is <code>SOURCE_LOG_GROUP</code>, because results are written back to the trace source log group. The name can't be under the service-reserved <code>/aws/bedrock-agentcore/evaluations/</code> namespace, apart from the service-managed default group.</p>"""
    log_stream_name: "capo_bedrock_agentcore.types.log_stream_name.LogStreamName"
    """<p>The name of the CloudWatch log stream where evaluation results will be written.</p>"""
    metrics_namespace: NotRequired[
        "capo_bedrock_agentcore.types.metrics_namespace.MetricsNamespace"
    ]
    """<p>The CloudWatch metrics namespace where evaluation result metrics are published. If you omit this value, the service publishes metrics to <code>Bedrock-AgentCore/Evaluations</code>. This value can't begin with <code>AWS/</code>.</p>"""
    result_destination: (
        "capo_bedrock_agentcore.types.result_destination.ResultDestination"
    )
    """<p>The destination where evaluation results are written. Valid values:</p> <ul> <li> <p> <code>DEDICATED_LOG_GROUP</code> (default) – Writes results to a dedicated result log group.</p> </li> <li> <p> <code>SOURCE_LOG_GROUP</code> – Writes results back to the log group that the agent traces were read from. If you use this value, don't specify <code>logGroupName</code>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchOutputConfig) -> dict:
    out: dict = {}
    out["logGroupName"] = value.get("log_group_name", "")
    out["logStreamName"] = value.get("log_stream_name", "")
    if "metrics_namespace" in value:
        out["metricsNamespace"] = value["metrics_namespace"]
    import capo_bedrock_agentcore.types.result_destination

    out["resultDestination"] = (
        capo_bedrock_agentcore.types.result_destination.serialize_json(
            value.get("result_destination", "DEDICATED_LOG_GROUP")
        )
    )
    return out


def deserialize_json(data: dict) -> CloudWatchOutputConfig:
    out: CloudWatchOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("logStreamName") is not None:
        out["log_stream_name"] = data["logStreamName"]
    else:
        out["log_stream_name"] = ""
    if data.get("metricsNamespace") is not None:
        out["metrics_namespace"] = data["metricsNamespace"]
    if data.get("resultDestination") is not None:
        import capo_bedrock_agentcore.types.result_destination

        out["result_destination"] = (
            capo_bedrock_agentcore.types.result_destination.deserialize_json(
                data["resultDestination"]
            )
        )
    else:
        out["result_destination"] = "DEDICATED_LOG_GROUP"
    return out
