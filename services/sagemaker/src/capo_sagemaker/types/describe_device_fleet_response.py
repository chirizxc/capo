"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDeviceFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_fleet_arn
    import capo_sagemaker.types.device_fleet_description
    import capo_sagemaker.types.edge_output_config
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.iot_role_alias
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp


class DescribeDeviceFleetResponse(TypedDict, closed=True):
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet.</p>"""
    device_fleet_arn: NotRequired[
        "capo_sagemaker.types.device_fleet_arn.DeviceFleetArn"
    ]
    """<p>The The Amazon Resource Name (ARN) of the fleet.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.edge_output_config.EdgeOutputConfig"
    ]
    """<p>The output configuration for storing sampled data.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.device_fleet_description.DeviceFleetDescription"
    ]
    """<p>A description of the fleet.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Timestamp of when the device fleet was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Timestamp of when the device fleet was last updated.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that has access to Amazon Web Services Internet of Things (IoT).</p>"""
    iot_role_alias: NotRequired["capo_sagemaker.types.iot_role_alias.IotRoleAlias"]
    """<p>The Amazon Resource Name (ARN) alias created in Amazon Web Services Internet of Things (IoT).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeviceFleetResponse) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "device_fleet_arn" in value:
        out["DeviceFleetArn"] = value["device_fleet_arn"]
    if "output_config" in value:
        import capo_sagemaker.types.edge_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.edge_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "iot_role_alias" in value:
        out["IotRoleAlias"] = value["iot_role_alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeviceFleetResponse:
    out: DescribeDeviceFleetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DeviceFleetName") is not None:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if data.get("DeviceFleetArn") is not None:
        out["device_fleet_arn"] = data["DeviceFleetArn"]
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.edge_output_config

        out["output_config"] = (
            capo_sagemaker.types.edge_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("IotRoleAlias") is not None:
        out["iot_role_alias"] = data["IotRoleAlias"]
    return out
