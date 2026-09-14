"""Generated from Smithy shape ``com.amazonaws.ssmsap#Operation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_sap.types.arn
    import capo_ssm_sap.types.operation_id
    import capo_ssm_sap.types.operation_properties
    import capo_ssm_sap.types.operation_status
    import capo_ssm_sap.types.operation_type
    import capo_ssm_sap.types.resource_id
    import capo_ssm_sap.types.resource_type


class Operation(TypedDict, closed=True):
    id: NotRequired["capo_ssm_sap.types.operation_id.OperationId"]
    """<p>The ID of the operation.</p>"""
    type: NotRequired["capo_ssm_sap.types.operation_type.OperationType"]
    """<p>The type of the operation.</p>"""
    status: NotRequired["capo_ssm_sap.types.operation_status.OperationStatus"]
    """<p>The status of the operation.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the operation.</p>"""
    properties: NotRequired[
        "capo_ssm_sap.types.operation_properties.OperationProperties"
    ]
    """<p>The properties of the operation.</p>"""
    resource_type: NotRequired["capo_ssm_sap.types.resource_type.ResourceType"]
    """<p>The resource type of the operation.</p>"""
    resource_id: NotRequired["capo_ssm_sap.types.resource_id.ResourceId"]
    """<p>The resource ID of the operation.</p>"""
    resource_arn: NotRequired["capo_ssm_sap.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the operation.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time of the operation.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the operation.</p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p>The time at which the operation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Operation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "status" in value:
        import capo_ssm_sap.types.operation_status

        out["Status"] = capo_ssm_sap.types.operation_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "properties" in value:
        import capo_ssm_sap.types.operation_properties

        out["Properties"] = capo_ssm_sap.types.operation_properties.serialize_json(
            value["properties"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "start_time" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["StartTime"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["EndTime"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "last_updated_time" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["LastUpdatedTime"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Status") is not None:
        import capo_ssm_sap.types.operation_status

        out["status"] = capo_ssm_sap.types.operation_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Properties") is not None:
        import capo_ssm_sap.types.operation_properties

        out["properties"] = capo_ssm_sap.types.operation_properties.deserialize_json(
            data["Properties"]
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("StartTime") is not None:
        import capo_ssm_sap.types._prelude.timestamp

        out["start_time"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_ssm_sap.types._prelude.timestamp

        out["end_time"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["EndTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_ssm_sap.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_ssm_sap.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
