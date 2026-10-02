"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_state

AlertStateList: TypeAlias = list["capo_cloudwatchomni.types.alert_state.AlertState"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertStateList) -> list:
    import capo_cloudwatchomni.types.alert_state

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.alert_state.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AlertStateList:
    import capo_cloudwatchomni.types.alert_state

    out: AlertStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.alert_state.deserialize_cbor(item))
    return out
