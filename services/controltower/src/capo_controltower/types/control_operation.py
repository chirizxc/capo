"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.control_identifier
    import capo_controltower.types.control_operation_status
    import capo_controltower.types.control_operation_type
    import capo_controltower.types.operation_identifier
    import capo_controltower.types.target_identifier
    import capo_controltower.types.timestamp


class ControlOperation(TypedDict, closed=True):
    operation_type: NotRequired[
        "capo_controltower.types.control_operation_type.ControlOperationType"
    ]
    """<p>One of <code>ENABLE_CONTROL</code> or <code>DISABLE_CONTROL</code>.</p>"""
    start_time: NotRequired["capo_controltower.types.timestamp.Timestamp"]
    """<p>The time that the operation began.</p>"""
    end_time: NotRequired["capo_controltower.types.timestamp.Timestamp"]
    """<p>The time that the operation finished.</p>"""
    status: NotRequired[
        "capo_controltower.types.control_operation_status.ControlOperationStatus"
    ]
    """<p>One of <code>IN_PROGRESS</code>, <code>SUCEEDED</code>, or <code>FAILED</code>.</p>"""
    status_message: NotRequired["str"]
    """<p>If the operation result is <code>FAILED</code>, this string contains a message explaining why the operation failed.</p>"""
    operation_identifier: NotRequired[
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The identifier of the specified operation.</p>"""
    control_identifier: NotRequired[
        "capo_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The <code>controlIdentifier</code> of the control for the operation.</p>"""
    target_identifier: NotRequired[
        "capo_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The target upon which the control operation is working.</p>"""
    enabled_control_identifier: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The <code>controlIdentifier</code> of the enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperation) -> dict:
    out: dict = {}
    if "operation_type" in value:
        import capo_controltower.types.control_operation_type

        out["operationType"] = (
            capo_controltower.types.control_operation_type.serialize_json(
                value["operation_type"]
            )
        )
    if "start_time" in value:
        import capo_controltower._protocol.serialize

        out["startTime"] = capo_controltower._protocol.serialize.fmt_date_time(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_controltower._protocol.serialize

        out["endTime"] = capo_controltower._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    if "status" in value:
        import capo_controltower.types.control_operation_status

        out["status"] = capo_controltower.types.control_operation_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "operation_identifier" in value:
        out["operationIdentifier"] = value["operation_identifier"]
    if "control_identifier" in value:
        out["controlIdentifier"] = value["control_identifier"]
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "enabled_control_identifier" in value:
        out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> ControlOperation:
    out: ControlOperation = {}  # type: ignore[typeddict-item]
    if data.get("operationType") is not None:
        import capo_controltower.types.control_operation_type

        out["operation_type"] = (
            capo_controltower.types.control_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    if data.get("status") is not None:
        import capo_controltower.types.control_operation_status

        out["status"] = (
            capo_controltower.types.control_operation_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    if data.get("controlIdentifier") is not None:
        out["control_identifier"] = data["controlIdentifier"]
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    if data.get("enabledControlIdentifier") is not None:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    return out
