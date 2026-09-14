"""Generated from Smithy shape ``com.amazonaws.groundstation#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_capability_type
    import capo_groundstation.types.config_details
    import capo_groundstation.types.uuid


class Destination(TypedDict, closed=True):
    config_type: NotRequired[
        "capo_groundstation.types.config_capability_type.ConfigCapabilityType"
    ]
    """<p>Type of a <code>Config</code>.</p>"""
    config_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a <code>Config</code>.</p>"""
    config_details: NotRequired["capo_groundstation.types.config_details.ConfigDetails"]
    """<p>Additional details for a <code>Config</code>, if type is dataflow endpoint or antenna demod decode.</p>"""
    dataflow_destination_region: NotRequired["str"]
    """<p>Region of a dataflow destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "config_type" in value:
        import capo_groundstation.types.config_capability_type

        out["configType"] = (
            capo_groundstation.types.config_capability_type.serialize_json(
                value["config_type"]
            )
        )
    if "config_id" in value:
        out["configId"] = value["config_id"]
    if "config_details" in value:
        import capo_groundstation.types.config_details

        out["configDetails"] = capo_groundstation.types.config_details.serialize_json(
            value["config_details"]
        )
    if "dataflow_destination_region" in value:
        out["dataflowDestinationRegion"] = value["dataflow_destination_region"]
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if data.get("configType") is not None:
        import capo_groundstation.types.config_capability_type

        out["config_type"] = (
            capo_groundstation.types.config_capability_type.deserialize_json(
                data["configType"]
            )
        )
    if data.get("configId") is not None:
        out["config_id"] = data["configId"]
    if data.get("configDetails") is not None:
        import capo_groundstation.types.config_details

        out["config_details"] = (
            capo_groundstation.types.config_details.deserialize_json(
                data["configDetails"]
            )
        )
    if data.get("dataflowDestinationRegion") is not None:
        out["dataflow_destination_region"] = data["dataflowDestinationRegion"]
    return out
