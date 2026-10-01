"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateAlertOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert
    import capo_cloudwatchomni.types.arn


class CreateAlertOutput(TypedDict, closed=True):
    alert_arn: NotRequired["capo_cloudwatchomni.types.arn.Arn"]
    """Deprecated. Use `alert.alertArn`, which carries the same value. Kept so an existing caller keeps working while it moves to `alert`."""
    alert: "capo_cloudwatchomni.types.alert.Alert"
    """The alert that was created. The same `Alert` shape GetAlert returns, so a caller need not read the alert back to learn its timestamps or its minted alert id. {@code alert.state} is absent here — see the `state` member of `Alert`. Every other member is populated exactly as GetAlert populates it."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAlertOutput) -> dict:
    out: dict = {}
    if "alert_arn" in value:
        out["alertArn"] = value["alert_arn"]
    import capo_cloudwatchomni.types.alert

    out["alert"] = capo_cloudwatchomni.types.alert.serialize_cbor(value["alert"])
    return out


def deserialize_cbor(data: dict) -> CreateAlertOutput:
    out: CreateAlertOutput = {}  # type: ignore[typeddict-item]
    if data.get("alertArn") is not None:
        out["alert_arn"] = data["alertArn"]
    if data.get("alert") is not None:
        import capo_cloudwatchomni.types.alert

        out["alert"] = capo_cloudwatchomni.types.alert.deserialize_cbor(data["alert"])
    else:
        raise DeserializationError("CreateAlertOutput.alert required")
    return out
