"""Generated from Smithy shape ``com.amazonaws.iotwireless#DefaultSessionParametersMulticast``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.dl_dr
    import capo_iot_wireless.types.dl_freq


class DefaultSessionParametersMulticast(TypedDict, closed=True):
    dl_dr: NotRequired["capo_iot_wireless.types.dl_dr.DlDr"]
    dl_freq: NotRequired["capo_iot_wireless.types.dl_freq.DlFreq"]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultSessionParametersMulticast) -> dict:
    out: dict = {}
    if "dl_dr" in value:
        out["DlDr"] = value["dl_dr"]
    if "dl_freq" in value:
        out["DlFreq"] = value["dl_freq"]
    return out


def deserialize_json(data: dict) -> DefaultSessionParametersMulticast:
    out: DefaultSessionParametersMulticast = {}  # type: ignore[typeddict-item]
    if data.get("DlDr") is not None:
        out["dl_dr"] = data["DlDr"]
    if data.get("DlFreq") is not None:
        out["dl_freq"] = data["DlFreq"]
    return out
