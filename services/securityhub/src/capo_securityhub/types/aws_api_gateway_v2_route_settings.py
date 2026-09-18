"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayV2RouteSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.double
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsApiGatewayV2RouteSettings(TypedDict, closed=True):
    detailed_metrics_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether detailed metrics are enabled.</p>"""
    logging_level: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The logging level. The logging level affects the log entries that are pushed to CloudWatch Logs. Supported only for WebSocket APIs.</p> <p>If the logging level is <code>ERROR</code>, then the logs only include error-level entries.</p> <p>If the logging level is <code>INFO</code>, then the logs include both <code>ERROR</code> events and extra informational events.</p> <p>Valid values: <code>OFF</code> | <code>ERROR</code> | <code>INFO</code> </p>"""
    data_trace_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether data trace logging is enabled. Data trace logging affects the log entries that are pushed to CloudWatch Logs. Supported only for WebSocket APIs.</p>"""
    throttling_burst_limit: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The throttling burst limit.</p>"""
    throttling_rate_limit: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The throttling rate limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayV2RouteSettings) -> dict:
    out: dict = {}
    if "detailed_metrics_enabled" in value:
        out["DetailedMetricsEnabled"] = value["detailed_metrics_enabled"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    if "data_trace_enabled" in value:
        out["DataTraceEnabled"] = value["data_trace_enabled"]
    if "throttling_burst_limit" in value:
        out["ThrottlingBurstLimit"] = value["throttling_burst_limit"]
    if "throttling_rate_limit" in value:
        out["ThrottlingRateLimit"] = (
            "NaN"
            if value["throttling_rate_limit"] != value["throttling_rate_limit"]
            else "Infinity"
            if value["throttling_rate_limit"] == float("inf")
            else "-Infinity"
            if value["throttling_rate_limit"] == float("-inf")
            else value["throttling_rate_limit"]
        )
    return out


def deserialize_json(data: dict) -> AwsApiGatewayV2RouteSettings:
    out: AwsApiGatewayV2RouteSettings = {}  # type: ignore[typeddict-item]
    if data.get("DetailedMetricsEnabled") is not None:
        out["detailed_metrics_enabled"] = data["DetailedMetricsEnabled"]
    if data.get("LoggingLevel") is not None:
        out["logging_level"] = data["LoggingLevel"]
    if data.get("DataTraceEnabled") is not None:
        out["data_trace_enabled"] = data["DataTraceEnabled"]
    if data.get("ThrottlingBurstLimit") is not None:
        out["throttling_burst_limit"] = data["ThrottlingBurstLimit"]
    if data.get("ThrottlingRateLimit") is not None:
        out["throttling_rate_limit"] = float(data["ThrottlingRateLimit"])
    return out
