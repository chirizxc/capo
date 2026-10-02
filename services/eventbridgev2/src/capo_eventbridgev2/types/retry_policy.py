"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#RetryPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.nullable_integer
    import capo_eventbridgev2.types.retry_strategy


class RetryPolicy(TypedDict, closed=True):
    max_retry_attempts: NotRequired[
        "capo_eventbridgev2.types.nullable_integer.NullableInteger"
    ]
    """Maximum number of retry attempts (0-185, default: 5)."""
    max_event_age_in_seconds: NotRequired[
        "capo_eventbridgev2.types.nullable_integer.NullableInteger"
    ]
    """Maximum age of an event in seconds before it is discarded (60-86400, default: 300)."""
    retry_strategy: NotRequired["capo_eventbridgev2.types.retry_strategy.RetryStrategy"]
    """Strategy for determining which exceptions are retried. Default: ALL."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryPolicy) -> dict:
    out: dict = {}
    if "max_retry_attempts" in value:
        out["MaxRetryAttempts"] = value["max_retry_attempts"]
    if "max_event_age_in_seconds" in value:
        out["MaxEventAgeInSeconds"] = value["max_event_age_in_seconds"]
    if "retry_strategy" in value:
        import capo_eventbridgev2.types.retry_strategy

        out["RetryStrategy"] = capo_eventbridgev2.types.retry_strategy.serialize_cbor(
            value["retry_strategy"]
        )
    return out


def deserialize_cbor(data: dict) -> RetryPolicy:
    out: RetryPolicy = {}  # type: ignore[typeddict-item]
    if data.get("MaxRetryAttempts") is not None:
        out["max_retry_attempts"] = data["MaxRetryAttempts"]
    if data.get("MaxEventAgeInSeconds") is not None:
        out["max_event_age_in_seconds"] = data["MaxEventAgeInSeconds"]
    if data.get("RetryStrategy") is not None:
        import capo_eventbridgev2.types.retry_strategy

        out["retry_strategy"] = (
            capo_eventbridgev2.types.retry_strategy.deserialize_cbor(
                data["RetryStrategy"]
            )
        )
    return out
