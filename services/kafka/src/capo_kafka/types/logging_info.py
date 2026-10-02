"""Generated from Smithy shape ``com.amazonaws.kafka#LoggingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.authorizer_logs
    import capo_kafka.types.broker_logs


class LoggingInfo(TypedDict, closed=True):
    authorizer_logs: NotRequired["capo_kafka.types.authorizer_logs.AuthorizerLogs"]
    """<p>You can configure your MSK cluster to send authorizer logs to different destination types.</p>"""
    broker_logs: NotRequired["capo_kafka.types.broker_logs.BrokerLogs"]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingInfo) -> dict:
    out: dict = {}
    if "authorizer_logs" in value:
        import capo_kafka.types.authorizer_logs

        out["authorizerLogs"] = capo_kafka.types.authorizer_logs.serialize_json(
            value["authorizer_logs"]
        )
    if "broker_logs" in value:
        import capo_kafka.types.broker_logs

        out["brokerLogs"] = capo_kafka.types.broker_logs.serialize_json(
            value["broker_logs"]
        )
    return out


def deserialize_json(data: dict) -> LoggingInfo:
    out: LoggingInfo = {}  # type: ignore[typeddict-item]
    if data.get("authorizerLogs") is not None:
        import capo_kafka.types.authorizer_logs

        out["authorizer_logs"] = capo_kafka.types.authorizer_logs.deserialize_json(
            data["authorizerLogs"]
        )
    if data.get("brokerLogs") is not None:
        import capo_kafka.types.broker_logs

        out["broker_logs"] = capo_kafka.types.broker_logs.deserialize_json(
            data["brokerLogs"]
        )
    return out
