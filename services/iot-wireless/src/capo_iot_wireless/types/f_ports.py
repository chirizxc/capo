"""Generated from Smithy shape ``com.amazonaws.iotwireless#FPorts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.applications
    import capo_iot_wireless.types.f_port
    import capo_iot_wireless.types.positioning


class FPorts(TypedDict, closed=True):
    fuota: NotRequired["capo_iot_wireless.types.f_port.FPort"]
    multicast: NotRequired["capo_iot_wireless.types.f_port.FPort"]
    clock_sync: NotRequired["capo_iot_wireless.types.f_port.FPort"]
    positioning: NotRequired["capo_iot_wireless.types.positioning.Positioning"]
    """<p>FPort values for the GNSS, stream, and ClockSync functions of the positioning information.</p>"""
    applications: NotRequired["capo_iot_wireless.types.applications.Applications"]
    """<p>Optional LoRaWAN application information, which can be used for geolocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FPorts) -> dict:
    out: dict = {}
    if "fuota" in value:
        out["Fuota"] = value["fuota"]
    if "multicast" in value:
        out["Multicast"] = value["multicast"]
    if "clock_sync" in value:
        out["ClockSync"] = value["clock_sync"]
    if "positioning" in value:
        import capo_iot_wireless.types.positioning

        out["Positioning"] = capo_iot_wireless.types.positioning.serialize_json(
            value["positioning"]
        )
    if "applications" in value:
        import capo_iot_wireless.types.applications

        out["Applications"] = capo_iot_wireless.types.applications.serialize_json(
            value["applications"]
        )
    return out


def deserialize_json(data: dict) -> FPorts:
    out: FPorts = {}  # type: ignore[typeddict-item]
    if data.get("Fuota") is not None:
        out["fuota"] = data["Fuota"]
    if data.get("Multicast") is not None:
        out["multicast"] = data["Multicast"]
    if data.get("ClockSync") is not None:
        out["clock_sync"] = data["ClockSync"]
    if data.get("Positioning") is not None:
        import capo_iot_wireless.types.positioning

        out["positioning"] = capo_iot_wireless.types.positioning.deserialize_json(
            data["Positioning"]
        )
    if data.get("Applications") is not None:
        import capo_iot_wireless.types.applications

        out["applications"] = capo_iot_wireless.types.applications.deserialize_json(
            data["Applications"]
        )
    return out
