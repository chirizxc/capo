"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#StepFunctionsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.invocation_type
    import capo_eventbridgev2.types.string


class StepFunctionsParameters(TypedDict, closed=True):
    invocation_type: NotRequired[
        "capo_eventbridgev2.types.invocation_type.InvocationType"
    ]
    """Selects StartExecution (EVENT) or StartSyncExecution (REQUEST_RESPONSE) at delivery."""
    name: NotRequired["capo_eventbridgev2.types.string.String"]
    """Name for the execution. Must be unique per account/region/state machine. Accepts JSONata expression."""
    trace_header: NotRequired["capo_eventbridgev2.types.string.String"]
    """X-Ray trace header for distributed tracing. Accepts JSONata expression."""
    invocation_timeout_seconds: NotRequired["capo_eventbridgev2.types.string.String"]
    """Timeout in seconds for each invocation of the target (1-30). String-typed (not integer) so the value may be a JSONata expression."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StepFunctionsParameters) -> dict:
    out: dict = {}
    if "invocation_type" in value:
        import capo_eventbridgev2.types.invocation_type

        out["InvocationType"] = capo_eventbridgev2.types.invocation_type.serialize_cbor(
            value["invocation_type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "trace_header" in value:
        out["TraceHeader"] = value["trace_header"]
    if "invocation_timeout_seconds" in value:
        out["InvocationTimeoutSeconds"] = value["invocation_timeout_seconds"]
    return out


def deserialize_cbor(data: dict) -> StepFunctionsParameters:
    out: StepFunctionsParameters = {}  # type: ignore[typeddict-item]
    if data.get("InvocationType") is not None:
        import capo_eventbridgev2.types.invocation_type

        out["invocation_type"] = (
            capo_eventbridgev2.types.invocation_type.deserialize_cbor(
                data["InvocationType"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TraceHeader") is not None:
        out["trace_header"] = data["TraceHeader"]
    if data.get("InvocationTimeoutSeconds") is not None:
        out["invocation_timeout_seconds"] = data["InvocationTimeoutSeconds"]
    return out
