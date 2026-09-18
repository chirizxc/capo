"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_arn
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.participant_recording_state
    import capo_ivs_realtime.types.participant_state
    import capo_ivs_realtime.types.published
    import capo_ivs_realtime.types.redundant_ingest
    import capo_ivs_realtime.types.replication_state
    import capo_ivs_realtime.types.replication_type
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_session_id
    import capo_ivs_realtime.types.time
    import capo_ivs_realtime.types.user_id


class ParticipantSummary(TypedDict, closed=True):
    participant_id: NotRequired["capo_ivs_realtime.types.participant_id.ParticipantId"]
    """<p>Unique identifier for this participant, assigned by IVS.</p>"""
    user_id: NotRequired["capo_ivs_realtime.types.user_id.UserId"]
    """<p>Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information</i>.</p>"""
    state: NotRequired["capo_ivs_realtime.types.participant_state.ParticipantState"]
    """<p>Whether the participant is connected to or disconnected from the stage.</p>"""
    first_join_time: NotRequired["capo_ivs_realtime.types.time.Time"]
    """<p>ISO 8601 timestamp (returned as a string) when the participant first joined the stage session.</p>"""
    published: "capo_ivs_realtime.types.published.Published"
    """<p>Whether the participant ever published to the stage session.</p>"""
    recording_state: NotRequired[
        "capo_ivs_realtime.types.participant_recording_state.ParticipantRecordingState"
    ]
    """<p>The participant’s recording state.</p>"""
    replication_type: NotRequired[
        "capo_ivs_realtime.types.replication_type.ReplicationType"
    ]
    """<p>Indicates if the participant has been replicated to another stage or is a replica from another stage. Default: <code>NONE</code>. </p>"""
    replication_state: NotRequired[
        "capo_ivs_realtime.types.replication_state.ReplicationState"
    ]
    """<p>The participant's replication state.</p>"""
    source_stage_arn: NotRequired["capo_ivs_realtime.types.stage_arn.StageArn"]
    """<p>Source stage ARN from which this participant is replicated, if <code>replicationType</code> is <code>REPLICA</code>.</p>"""
    source_session_id: NotRequired[
        "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    ]
    """<p>ID of the session within the source stage, if <code>replicationType</code> is <code>REPLICA</code>.</p>"""
    redundant_ingest: "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
    """<p>Indicates whether redundant ingest is enabled for the participant.</p>"""
    ingest_configuration_arn: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    ]
    """<p>The participant’s ingest configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantSummary) -> dict:
    out: dict = {}
    if "participant_id" in value:
        out["participantId"] = value["participant_id"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "state" in value:
        out["state"] = value["state"]
    if "first_join_time" in value:
        import capo_ivs_realtime.types.time

        out["firstJoinTime"] = capo_ivs_realtime.types.time.serialize_json(
            value["first_join_time"]
        )
    out["published"] = value.get("published", False)
    if "recording_state" in value:
        out["recordingState"] = value["recording_state"]
    if "replication_type" in value:
        out["replicationType"] = value["replication_type"]
    if "replication_state" in value:
        out["replicationState"] = value["replication_state"]
    if "source_stage_arn" in value:
        out["sourceStageArn"] = value["source_stage_arn"]
    if "source_session_id" in value:
        out["sourceSessionId"] = value["source_session_id"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    if "ingest_configuration_arn" in value:
        out["ingestConfigurationArn"] = value["ingest_configuration_arn"]
    return out


def deserialize_json(data: dict) -> ParticipantSummary:
    out: ParticipantSummary = {}  # type: ignore[typeddict-item]
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("firstJoinTime") is not None:
        import capo_ivs_realtime.types.time

        out["first_join_time"] = capo_ivs_realtime.types.time.deserialize_json(
            data["firstJoinTime"]
        )
    if data.get("published") is not None:
        out["published"] = data["published"]
    else:
        out["published"] = False
    if data.get("recordingState") is not None:
        out["recording_state"] = data["recordingState"]
    if data.get("replicationType") is not None:
        out["replication_type"] = data["replicationType"]
    if data.get("replicationState") is not None:
        out["replication_state"] = data["replicationState"]
    if data.get("sourceStageArn") is not None:
        out["source_stage_arn"] = data["sourceStageArn"]
    if data.get("sourceSessionId") is not None:
        out["source_session_id"] = data["sourceSessionId"]
    if data.get("redundantIngest") is not None:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    if data.get("ingestConfigurationArn") is not None:
        out["ingest_configuration_arn"] = data["ingestConfigurationArn"]
    return out
