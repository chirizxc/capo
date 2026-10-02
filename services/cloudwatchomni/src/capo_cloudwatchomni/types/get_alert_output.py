"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetAlertOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert


class GetAlertOutput(TypedDict, closed=True):
    alert: "capo_cloudwatchomni.types.alert.Alert"
    """The full alert entity."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAlertOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.alert

    out["alert"] = capo_cloudwatchomni.types.alert.serialize_cbor(value["alert"])
    return out


def deserialize_cbor(data: dict) -> GetAlertOutput:
    out: GetAlertOutput = {}  # type: ignore[typeddict-item]
    if data.get("alert") is not None:
        import capo_cloudwatchomni.types.alert

        out["alert"] = capo_cloudwatchomni.types.alert.deserialize_cbor(data["alert"])
    else:
        raise DeserializationError("GetAlertOutput.alert required")
    return out
