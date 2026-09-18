"""Generated from Smithy shape ``com.amazonaws.devicefarm#Radios``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.boolean


class Radios(TypedDict, closed=True):
    wifi: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.</p>"""
    bluetooth: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>True if Bluetooth is enabled at the beginning of the test. Otherwise, false.</p>"""
    nfc: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>True if NFC is enabled at the beginning of the test. Otherwise, false.</p>"""
    gps: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>True if GPS is enabled at the beginning of the test. Otherwise, false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Radios) -> dict:
    out: dict = {}
    if "wifi" in value:
        out["wifi"] = value["wifi"]
    if "bluetooth" in value:
        out["bluetooth"] = value["bluetooth"]
    if "nfc" in value:
        out["nfc"] = value["nfc"]
    if "gps" in value:
        out["gps"] = value["gps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Radios:
    out: Radios = {}  # type: ignore[typeddict-item]
    if data.get("wifi") is not None:
        out["wifi"] = data["wifi"]
    if data.get("bluetooth") is not None:
        out["bluetooth"] = data["bluetooth"]
    if data.get("nfc") is not None:
        out["nfc"] = data["nfc"]
    if data.get("gps") is not None:
        out["gps"] = data["gps"]
    return out
