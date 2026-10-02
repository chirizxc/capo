"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.include_payload
    import capo_eventbridgev2.types.log_level


class LogConfiguration(TypedDict, closed=True):
    level: NotRequired["capo_eventbridgev2.types.log_level.LogLevel"]
    """Minimum log level. Records below this level are not emitted. Defaults to OFF."""
    include_payload: NotRequired[
        "capo_eventbridgev2.types.include_payload.IncludePayload"
    ]
    """Whether the customer event payload is embedded in log records. Defaults to ON_ERROR_ONLY."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogConfiguration) -> dict:
    out: dict = {}
    if "level" in value:
        import capo_eventbridgev2.types.log_level

        out["Level"] = capo_eventbridgev2.types.log_level.serialize_cbor(value["level"])
    if "include_payload" in value:
        import capo_eventbridgev2.types.include_payload

        out["IncludePayload"] = capo_eventbridgev2.types.include_payload.serialize_cbor(
            value["include_payload"]
        )
    return out


def deserialize_cbor(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Level") is not None:
        import capo_eventbridgev2.types.log_level

        out["level"] = capo_eventbridgev2.types.log_level.deserialize_cbor(
            data["Level"]
        )
    if data.get("IncludePayload") is not None:
        import capo_eventbridgev2.types.include_payload

        out["include_payload"] = (
            capo_eventbridgev2.types.include_payload.deserialize_cbor(
                data["IncludePayload"]
            )
        )
    return out
