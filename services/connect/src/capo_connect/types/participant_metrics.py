"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.count
    import capo_connect.types.duration_millis
    import capo_connect.types.nullable_boolean
    import capo_connect.types.participant_id
    import capo_connect.types.participant_type
    import capo_connect.types.timestamp


class ParticipantMetrics(TypedDict, closed=True):
    participant_id: NotRequired["capo_connect.types.participant_id.ParticipantId"]
    """<p>The Participant's ID.</p>"""
    participant_type: NotRequired["capo_connect.types.participant_type.ParticipantType"]
    """<p>Information about the conversation participant. Following are the participant types: [Agent, Customer, Supervisor].</p>"""
    conversation_abandon: NotRequired[
        "capo_connect.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A boolean flag indicating whether the chat conversation was abandoned by a Participant.</p>"""
    messages_sent: NotRequired["capo_connect.types.count.Count"]
    """<p>Number of chat messages sent by Participant.</p>"""
    num_responses: NotRequired["capo_connect.types.count.Count"]
    """<p>Number of chat messages sent by Participant.</p>"""
    message_length_in_chars: NotRequired["capo_connect.types.count.Count"]
    """<p>Number of chat characters sent by Participant.</p>"""
    total_response_time_in_millis: NotRequired[
        "capo_connect.types.duration_millis.DurationMillis"
    ]
    """<p>Total chat response time by Participant.</p>"""
    max_response_time_in_millis: NotRequired[
        "capo_connect.types.duration_millis.DurationMillis"
    ]
    """<p>Maximum chat response time by Participant.</p>"""
    last_message_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>Timestamp of last chat message by Participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantMetrics) -> dict:
    out: dict = {}
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "participant_type" in value:
        import capo_connect.types.participant_type

        out["ParticipantType"] = capo_connect.types.participant_type.serialize_json(
            value["participant_type"]
        )
    if "conversation_abandon" in value:
        out["ConversationAbandon"] = value["conversation_abandon"]
    if "messages_sent" in value:
        out["MessagesSent"] = value["messages_sent"]
    if "num_responses" in value:
        out["NumResponses"] = value["num_responses"]
    if "message_length_in_chars" in value:
        out["MessageLengthInChars"] = value["message_length_in_chars"]
    if "total_response_time_in_millis" in value:
        out["TotalResponseTimeInMillis"] = value["total_response_time_in_millis"]
    if "max_response_time_in_millis" in value:
        out["MaxResponseTimeInMillis"] = value["max_response_time_in_millis"]
    if "last_message_timestamp" in value:
        import capo_connect.types.timestamp

        out["LastMessageTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["last_message_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ParticipantMetrics:
    out: ParticipantMetrics = {}  # type: ignore[typeddict-item]
    if data.get("ParticipantId") is not None:
        out["participant_id"] = data["ParticipantId"]
    if data.get("ParticipantType") is not None:
        import capo_connect.types.participant_type

        out["participant_type"] = capo_connect.types.participant_type.deserialize_json(
            data["ParticipantType"]
        )
    if data.get("ConversationAbandon") is not None:
        out["conversation_abandon"] = data["ConversationAbandon"]
    if data.get("MessagesSent") is not None:
        out["messages_sent"] = data["MessagesSent"]
    if data.get("NumResponses") is not None:
        out["num_responses"] = data["NumResponses"]
    if data.get("MessageLengthInChars") is not None:
        out["message_length_in_chars"] = data["MessageLengthInChars"]
    if data.get("TotalResponseTimeInMillis") is not None:
        out["total_response_time_in_millis"] = data["TotalResponseTimeInMillis"]
    if data.get("MaxResponseTimeInMillis") is not None:
        out["max_response_time_in_millis"] = data["MaxResponseTimeInMillis"]
    if data.get("LastMessageTimestamp") is not None:
        import capo_connect.types.timestamp

        out["last_message_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["LastMessageTimestamp"]
        )
    return out
