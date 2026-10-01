"""Generated from Smithy shape ``com.amazonaws.synthetics#MultiLocationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.location
    import capo_synthetics.types.location_type
    import capo_synthetics.types.replicas
    import capo_synthetics.types.replication_state


class MultiLocationConfig(TypedDict, closed=True):
    location_type: NotRequired["capo_synthetics.types.location_type.LocationType"]
    """<p>Indicates whether this canary is the <code>Primary</code> or a <code>Replica</code> in the multi-location configuration.</p>"""
    primary_location: NotRequired["capo_synthetics.types.location.Location"]
    """<p>The Amazon Web Services Region where the primary canary is located.</p>"""
    replicas: NotRequired["capo_synthetics.types.replicas.Replicas"]
    """<p>A list of replicas for this canary. This field is present only for the primary location canary.</p>"""
    replication_state: NotRequired[
        "capo_synthetics.types.replication_state.ReplicationState"
    ]
    """<p>The overall replication state of the canary across all replica locations. This field is present only for the primary location canary. Valid values are <code>InProgress</code>, <code>InSync</code>, and <code>Inconsistent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiLocationConfig) -> dict:
    out: dict = {}
    if "location_type" in value:
        import capo_synthetics.types.location_type

        out["LocationType"] = capo_synthetics.types.location_type.serialize_json(
            value["location_type"]
        )
    if "primary_location" in value:
        out["PrimaryLocation"] = value["primary_location"]
    if "replicas" in value:
        import capo_synthetics.types.replicas

        out["Replicas"] = capo_synthetics.types.replicas.serialize_json(
            value["replicas"]
        )
    if "replication_state" in value:
        import capo_synthetics.types.replication_state

        out["ReplicationState"] = (
            capo_synthetics.types.replication_state.serialize_json(
                value["replication_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiLocationConfig:
    out: MultiLocationConfig = {}  # type: ignore[typeddict-item]
    if data.get("LocationType") is not None:
        import capo_synthetics.types.location_type

        out["location_type"] = capo_synthetics.types.location_type.deserialize_json(
            data["LocationType"]
        )
    if data.get("PrimaryLocation") is not None:
        out["primary_location"] = data["PrimaryLocation"]
    if data.get("Replicas") is not None:
        import capo_synthetics.types.replicas

        out["replicas"] = capo_synthetics.types.replicas.deserialize_json(
            data["Replicas"]
        )
    if data.get("ReplicationState") is not None:
        import capo_synthetics.types.replication_state

        out["replication_state"] = (
            capo_synthetics.types.replication_state.deserialize_json(
                data["ReplicationState"]
            )
        )
    return out
