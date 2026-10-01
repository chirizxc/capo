"""Generated from Smithy shape ``com.amazonaws.iotwireless#GnssCaptures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.gnss_capture

GnssCaptures: TypeAlias = list["capo_iot_wireless.types.gnss_capture.GnssCapture"]


# --- restJson1 ser/de ---
def serialize_json(value: GnssCaptures) -> list:
    import capo_iot_wireless.types.gnss_capture

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.gnss_capture.serialize_json(item))
    return out


def deserialize_json(data: list) -> GnssCaptures:
    import capo_iot_wireless.types.gnss_capture

    out: GnssCaptures = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iot_wireless.types.gnss_capture.deserialize_json(item))
    return out
