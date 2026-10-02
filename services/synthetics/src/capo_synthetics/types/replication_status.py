"""Generated from Smithy shape ``com.amazonaws.synthetics#ReplicationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.replication_state
    import capo_synthetics.types.string


class ReplicationStatus(TypedDict, closed=True):
    state: NotRequired["capo_synthetics.types.replication_state.ReplicationState"]
    """<p>The replication state of the replica. Valid values are <code>InProgress</code>, <code>InSync</code>, and <code>Inconsistent</code>.</p>"""
    state_reason: NotRequired["capo_synthetics.types.string.String"]
    """<p>A description that provides more detail about the current replication state.</p>"""
    state_reason_code: NotRequired["capo_synthetics.types.string.String"]
    """<p>A code that provides more detail about the current replication state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_synthetics.types.replication_state

        out["State"] = capo_synthetics.types.replication_state.serialize_json(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_code" in value:
        out["StateReasonCode"] = value["state_reason_code"]
    return out


def deserialize_json(data: dict) -> ReplicationStatus:
    out: ReplicationStatus = {}  # type: ignore[typeddict-item]
    if data.get("State") is not None:
        import capo_synthetics.types.replication_state

        out["state"] = capo_synthetics.types.replication_state.deserialize_json(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonCode") is not None:
        out["state_reason_code"] = data["StateReasonCode"]
    return out
