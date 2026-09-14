"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANMulticastGet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.dl_class
    import capo_iot_wireless.types.number_of_devices_in_group
    import capo_iot_wireless.types.number_of_devices_requested
    import capo_iot_wireless.types.participating_gateways_multicast
    import capo_iot_wireless.types.supported_rf_region


class LoRaWANMulticastGet(TypedDict, closed=True):
    rf_region: NotRequired[
        "capo_iot_wireless.types.supported_rf_region.SupportedRfRegion"
    ]
    dl_class: NotRequired["capo_iot_wireless.types.dl_class.DlClass"]
    number_of_devices_requested: NotRequired[
        "capo_iot_wireless.types.number_of_devices_requested.NumberOfDevicesRequested"
    ]
    number_of_devices_in_group: NotRequired[
        "capo_iot_wireless.types.number_of_devices_in_group.NumberOfDevicesInGroup"
    ]
    participating_gateways: NotRequired[
        "capo_iot_wireless.types.participating_gateways_multicast.ParticipatingGatewaysMulticast"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANMulticastGet) -> dict:
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
    if "number_of_devices_requested" in value:
        out["NumberOfDevicesRequested"] = value["number_of_devices_requested"]
    if "number_of_devices_in_group" in value:
        out["NumberOfDevicesInGroup"] = value["number_of_devices_in_group"]
    if "participating_gateways" in value:
        import capo_iot_wireless.types.participating_gateways_multicast

        out["ParticipatingGateways"] = (
            capo_iot_wireless.types.participating_gateways_multicast.serialize_json(
                value["participating_gateways"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANMulticastGet:
    out: LoRaWANMulticastGet = {}  # type: ignore[typeddict-item]
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
    if data.get("NumberOfDevicesRequested") is not None:
        out["number_of_devices_requested"] = data["NumberOfDevicesRequested"]
    if data.get("NumberOfDevicesInGroup") is not None:
        out["number_of_devices_in_group"] = data["NumberOfDevicesInGroup"]
    if data.get("ParticipatingGateways") is not None:
        import capo_iot_wireless.types.participating_gateways_multicast

        out["participating_gateways"] = (
            capo_iot_wireless.types.participating_gateways_multicast.deserialize_json(
                data["ParticipatingGateways"]
            )
        )
    return out
