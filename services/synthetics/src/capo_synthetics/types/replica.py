"""Generated from Smithy shape ``com.amazonaws.synthetics#Replica``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canary_state
    import capo_synthetics.types.location
    import capo_synthetics.types.replication_status
    import capo_synthetics.types.timestamp
    import capo_synthetics.types.vpc_config_output


class Replica(TypedDict, closed=True):
    location: NotRequired["capo_synthetics.types.location.Location"]
    """<p>The Amazon Web Services Region where this replica is located.</p>"""
    replication_status: NotRequired[
        "capo_synthetics.types.replication_status.ReplicationStatus"
    ]
    """<p>A structure that contains information about the replication status of this replica.</p>"""
    canary_state: NotRequired["capo_synthetics.types.canary_state.CanaryState"]
    """<p>The current state of the canary in this replica location.</p>"""
    last_modified: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time that the replica was last modified.</p>"""
    vpc_config: NotRequired["capo_synthetics.types.vpc_config_output.VpcConfigOutput"]
    """<p>The VPC configuration for the canary replica in this location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Replica) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "replication_status" in value:
        import capo_synthetics.types.replication_status

        out["ReplicationStatus"] = (
            capo_synthetics.types.replication_status.serialize_json(
                value["replication_status"]
            )
        )
    if "canary_state" in value:
        import capo_synthetics.types.canary_state

        out["CanaryState"] = capo_synthetics.types.canary_state.serialize_json(
            value["canary_state"]
        )
    if "last_modified" in value:
        import capo_synthetics.types.timestamp

        out["LastModified"] = capo_synthetics.types.timestamp.serialize_json(
            value["last_modified"]
        )
    if "vpc_config" in value:
        import capo_synthetics.types.vpc_config_output

        out["VpcConfig"] = capo_synthetics.types.vpc_config_output.serialize_json(
            value["vpc_config"]
        )
    return out


def deserialize_json(data: dict) -> Replica:
    out: Replica = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ReplicationStatus") is not None:
        import capo_synthetics.types.replication_status

        out["replication_status"] = (
            capo_synthetics.types.replication_status.deserialize_json(
                data["ReplicationStatus"]
            )
        )
    if data.get("CanaryState") is not None:
        import capo_synthetics.types.canary_state

        out["canary_state"] = capo_synthetics.types.canary_state.deserialize_json(
            data["CanaryState"]
        )
    if data.get("LastModified") is not None:
        import capo_synthetics.types.timestamp

        out["last_modified"] = capo_synthetics.types.timestamp.deserialize_json(
            data["LastModified"]
        )
    if data.get("VpcConfig") is not None:
        import capo_synthetics.types.vpc_config_output

        out["vpc_config"] = capo_synthetics.types.vpc_config_output.deserialize_json(
            data["VpcConfig"]
        )
    return out
