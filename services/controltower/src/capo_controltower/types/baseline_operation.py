"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.baseline_operation_status
    import capo_controltower.types.baseline_operation_type
    import capo_controltower.types.operation_identifier
    import capo_controltower.types.timestamp


class BaselineOperation(TypedDict, closed=True):
    operation_identifier: NotRequired[
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The identifier of the specified operation.</p>"""
    operation_type: NotRequired[
        "capo_controltower.types.baseline_operation_type.BaselineOperationType"
    ]
    """<p>An enumerated type (<code>enum</code>) with possible values of <code>ENABLE_BASELINE</code>, <code>DISABLE_BASELINE</code>, <code>UPDATE_ENABLED_BASELINE</code>, or <code>RESET_ENABLED_BASELINE</code>.</p>"""
    status: NotRequired[
        "capo_controltower.types.baseline_operation_status.BaselineOperationStatus"
    ]
    """<p>An enumerated type (<code>enum</code>) with possible values of <code>SUCCEEDED</code>, <code>FAILED</code>, or <code>IN_PROGRESS</code>.</p>"""
    start_time: NotRequired["capo_controltower.types.timestamp.Timestamp"]
    """<p>The start time of the operation, in ISO 8601 format.</p>"""
    end_time: NotRequired["capo_controltower.types.timestamp.Timestamp"]
    """<p>The end time of the operation (if applicable), in ISO 8601 format.</p>"""
    status_message: NotRequired["str"]
    """<p>A status message that gives more information about the operation's status, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaselineOperation) -> dict:
    out: dict = {}
    if "operation_identifier" in value:
        out["operationIdentifier"] = value["operation_identifier"]
    if "operation_type" in value:
        import capo_controltower.types.baseline_operation_type

        out["operationType"] = (
            capo_controltower.types.baseline_operation_type.serialize_json(
                value["operation_type"]
            )
        )
    if "status" in value:
        import capo_controltower.types.baseline_operation_status

        out["status"] = (
            capo_controltower.types.baseline_operation_status.serialize_json(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_controltower.types.timestamp

        out["startTime"] = capo_controltower.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_controltower.types.timestamp

        out["endTime"] = capo_controltower.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> BaselineOperation:
    out: BaselineOperation = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    if data.get("operationType") is not None:
        import capo_controltower.types.baseline_operation_type

        out["operation_type"] = (
            capo_controltower.types.baseline_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    if data.get("status") is not None:
        import capo_controltower.types.baseline_operation_status

        out["status"] = (
            capo_controltower.types.baseline_operation_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("startTime") is not None:
        import capo_controltower.types.timestamp

        out["start_time"] = capo_controltower.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_controltower.types.timestamp

        out["end_time"] = capo_controltower.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
