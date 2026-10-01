"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANMulticast``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.default_session_parameters_multicast
    import capo_iot_wireless.types.dl_class
    import capo_iot_wireless.types.participating_gateways_multicast
    import capo_iot_wireless.types.supported_rf_region


class LoRaWANMulticast(TypedDict, closed=True):
    rf_region: NotRequired[
        "capo_iot_wireless.types.supported_rf_region.SupportedRfRegion"
    ]
    dl_class: NotRequired["capo_iot_wireless.types.dl_class.DlClass"]
    participating_gateways: NotRequired[
        "capo_iot_wireless.types.participating_gateways_multicast.ParticipatingGatewaysMulticast"
    ]
    default_session_parameters: NotRequired[
        "capo_iot_wireless.types.default_session_parameters_multicast.DefaultSessionParametersMulticast"
    ]
    """<p>The default session parameters for the multicast group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANMulticast) -> dict:
    out: dict = {}
    if "rf_region" in value:
        import capo_iot_wireless.types.supported_rf_region

        out["RfRegion"] = capo_iot_wireless.types.supported_rf_region.serialize_json(
            value["rf_region"]
        )
    if "dl_class" in value:
        import capo_iot_wireless.types.dl_class

        out["DlClass"] = capo_iot_wireless.types.dl_class.serialize_json(
            value["dl_class"]
        )
    if "participating_gateways" in value:
        import capo_iot_wireless.types.participating_gateways_multicast

        out["ParticipatingGateways"] = (
            capo_iot_wireless.types.participating_gateways_multicast.serialize_json(
                value["participating_gateways"]
            )
        )
    if "default_session_parameters" in value:
        import capo_iot_wireless.types.default_session_parameters_multicast

        out["DefaultSessionParameters"] = (
            capo_iot_wireless.types.default_session_parameters_multicast.serialize_json(
                value["default_session_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANMulticast:
    out: LoRaWANMulticast = {}  # type: ignore[typeddict-item]
    if data.get("RfRegion") is not None:
        import capo_iot_wireless.types.supported_rf_region

        out["rf_region"] = capo_iot_wireless.types.supported_rf_region.deserialize_json(
            data["RfRegion"]
        )
    if data.get("DlClass") is not None:
        import capo_iot_wireless.types.dl_class

        out["dl_class"] = capo_iot_wireless.types.dl_class.deserialize_json(
            data["DlClass"]
        )
    if data.get("ParticipatingGateways") is not None:
        import capo_iot_wireless.types.participating_gateways_multicast

        out["participating_gateways"] = (
            capo_iot_wireless.types.participating_gateways_multicast.deserialize_json(
                data["ParticipatingGateways"]
            )
        )
    if data.get("DefaultSessionParameters") is not None:
        import capo_iot_wireless.types.default_session_parameters_multicast

        out["default_session_parameters"] = (
            capo_iot_wireless.types.default_session_parameters_multicast.deserialize_json(
                data["DefaultSessionParameters"]
            )
        )
    return out
