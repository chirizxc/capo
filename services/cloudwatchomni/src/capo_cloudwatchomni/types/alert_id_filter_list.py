"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_id

AlertIdFilterList: TypeAlias = list["capo_cloudwatchomni.types.alert_id.AlertId"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertIdFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AlertIdFilterList:
    return [item for item in data if item is not None]
