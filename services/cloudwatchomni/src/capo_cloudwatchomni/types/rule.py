"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Rule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.telemetry_rule


class _Rule_telemetryRule(TypedDict, closed=True):
    telemetryRule: "capo_cloudwatchomni.types.telemetry_rule.TelemetryRule"


Rule: TypeAlias = _Rule_telemetryRule


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Rule) -> dict:
    if "telemetryRule" in value:
        import capo_cloudwatchomni.types.telemetry_rule

        return {
            "telemetryRule": capo_cloudwatchomni.types.telemetry_rule.serialize_cbor(
                value["telemetryRule"]
            )
        }
    else:
        raise SerializationError("Rule: no variant present")


def deserialize_cbor(data: dict) -> Rule:
    if data.get("telemetryRule") is not None:
        import capo_cloudwatchomni.types.telemetry_rule

        return {
            "telemetryRule": capo_cloudwatchomni.types.telemetry_rule.deserialize_cbor(
                data["telemetryRule"]
            )
        }
    else:
        raise DeserializationError("Rule: no recognized variant key")
