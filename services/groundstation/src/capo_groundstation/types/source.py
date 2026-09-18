"""Generated from Smithy shape ``com.amazonaws.groundstation#Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_capability_type
    import capo_groundstation.types.config_details


class Source(TypedDict, closed=True):
    config_type: NotRequired[
        "capo_groundstation.types.config_capability_type.ConfigCapabilityType"
    ]
    """<p>Type of a <code>Config</code>.</p>"""
    config_id: NotRequired["str"]
    """<p>UUID of a <code>Config</code>.</p>"""
    config_details: NotRequired["capo_groundstation.types.config_details.ConfigDetails"]
    """<p>Additional details for a <code>Config</code>, if type is <code>dataflow-endpoint</code> or <code>antenna-downlink-demod-decode</code> </p>"""
    dataflow_source_region: NotRequired["str"]
    """<p>Region of a dataflow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
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
    if "dataflow_source_region" in value:
        out["dataflowSourceRegion"] = value["dataflow_source_region"]
    return out


def deserialize_json(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
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
    if data.get("dataflowSourceRegion") is not None:
        out["dataflow_source_region"] = data["dataflowSourceRegion"]
    return out
