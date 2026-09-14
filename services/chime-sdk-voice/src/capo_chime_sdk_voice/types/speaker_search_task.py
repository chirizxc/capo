"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.call_details
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.speaker_search_details
    import capo_chime_sdk_voice.types.string


class SpeakerSearchTask(TypedDict, closed=True):
    speaker_search_task_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The speaker search task ID.</p>"""
    speaker_search_task_status: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the speaker search task, <code>IN_QUEUE</code>, <code>IN_PROGRESS</code>, <code>PARTIAL_SUCCESS</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, or <code>STOPPED</code>.</p>"""
    call_details: NotRequired["capo_chime_sdk_voice.types.call_details.CallDetails"]
    """<p>The call details of a speaker search task.</p>"""
    speaker_search_details: NotRequired[
        "capo_chime_sdk_voice.types.speaker_search_details.SpeakerSearchDetails"
    ]
    """<p>The details of a speaker search task.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a speaker search task was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a speaker search task was updated.</p>"""
    started_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the speaker search task began.</p>"""
    status_message: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>A detailed message about the status of a speaker search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchTask) -> dict:
    out: dict = {}
    if "speaker_search_task_id" in value:
        out["SpeakerSearchTaskId"] = value["speaker_search_task_id"]
    if "speaker_search_task_status" in value:
        out["SpeakerSearchTaskStatus"] = value["speaker_search_task_status"]
    if "call_details" in value:
        import capo_chime_sdk_voice.types.call_details

        out["CallDetails"] = capo_chime_sdk_voice.types.call_details.serialize_json(
            value["call_details"]
        )
    if "speaker_search_details" in value:
        import capo_chime_sdk_voice.types.speaker_search_details

        out["SpeakerSearchDetails"] = (
            capo_chime_sdk_voice.types.speaker_search_details.serialize_json(
                value["speaker_search_details"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "started_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["StartedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["started_timestamp"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> SpeakerSearchTask:
    out: SpeakerSearchTask = {}  # type: ignore[typeddict-item]
    if data.get("SpeakerSearchTaskId") is not None:
        out["speaker_search_task_id"] = data["SpeakerSearchTaskId"]
    if data.get("SpeakerSearchTaskStatus") is not None:
        out["speaker_search_task_status"] = data["SpeakerSearchTaskStatus"]
    if data.get("CallDetails") is not None:
        import capo_chime_sdk_voice.types.call_details

        out["call_details"] = capo_chime_sdk_voice.types.call_details.deserialize_json(
            data["CallDetails"]
        )
    if data.get("SpeakerSearchDetails") is not None:
        import capo_chime_sdk_voice.types.speaker_search_details

        out["speaker_search_details"] = (
            capo_chime_sdk_voice.types.speaker_search_details.deserialize_json(
                data["SpeakerSearchDetails"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if data.get("StartedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["started_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["StartedTimestamp"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
