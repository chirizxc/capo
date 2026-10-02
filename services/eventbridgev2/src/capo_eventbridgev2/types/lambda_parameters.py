"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#LambdaParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.invocation_type
    import capo_eventbridgev2.types.string


class LambdaParameters(TypedDict, closed=True):
    invocation_type: NotRequired[
        "capo_eventbridgev2.types.invocation_type.InvocationType"
    ]
    """Lambda invocation type. EVENT invokes the function asynchronously; REQUEST_RESPONSE waits for its result."""
    qualifier: NotRequired["capo_eventbridgev2.types.string.String"]
    """Lambda qualifier: $LATEST, $LATEST.PUBLISHED, a numeric version, or an alias. Accepts a JSONata expression."""
    durable_execution_name: NotRequired["capo_eventbridgev2.types.string.String"]
    """Durable execution name. Accepts a JSONata expression."""
    tenant_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Tenant identifier. Accepts a JSONata expression."""
    invocation_timeout_seconds: NotRequired["capo_eventbridgev2.types.string.String"]
    """Timeout in seconds for each invocation of the target. String-typed so the value may be a JSONata expression."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaParameters) -> dict:
    out: dict = {}
    if "invocation_type" in value:
        import capo_eventbridgev2.types.invocation_type

        out["InvocationType"] = capo_eventbridgev2.types.invocation_type.serialize_cbor(
            value["invocation_type"]
        )
    if "qualifier" in value:
        out["Qualifier"] = value["qualifier"]
    if "durable_execution_name" in value:
        out["DurableExecutionName"] = value["durable_execution_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "invocation_timeout_seconds" in value:
        out["InvocationTimeoutSeconds"] = value["invocation_timeout_seconds"]
    return out


def deserialize_cbor(data: dict) -> LambdaParameters:
    out: LambdaParameters = {}  # type: ignore[typeddict-item]
    if data.get("InvocationType") is not None:
        import capo_eventbridgev2.types.invocation_type

        out["invocation_type"] = (
            capo_eventbridgev2.types.invocation_type.deserialize_cbor(
                data["InvocationType"]
            )
        )
    if data.get("Qualifier") is not None:
        out["qualifier"] = data["Qualifier"]
    if data.get("DurableExecutionName") is not None:
        out["durable_execution_name"] = data["DurableExecutionName"]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("InvocationTimeoutSeconds") is not None:
        out["invocation_timeout_seconds"] = data["InvocationTimeoutSeconds"]
    return out
