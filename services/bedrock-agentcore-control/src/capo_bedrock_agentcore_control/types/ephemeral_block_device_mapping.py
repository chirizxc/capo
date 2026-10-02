"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EphemeralBlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.device_name
    import capo_bedrock_agentcore_control.types.ephemeral_ebs_volume_configuration
    import capo_bedrock_agentcore_control.types.virtual_device_name


class EphemeralBlockDeviceMapping(TypedDict, closed=True):
    device_name: NotRequired[
        "capo_bedrock_agentcore_control.types.device_name.DeviceName"
    ]
    """<p>The device name, for example <code>/dev/sdh</code> or <code>xvdh</code>.</p>"""
    virtual_name: NotRequired[
        "capo_bedrock_agentcore_control.types.virtual_device_name.VirtualDeviceName"
    ]
    """<p>The virtual device name (<code>ephemeralN</code>). Instance store volumes are numbered starting from 0. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.</p>"""
    ebs: NotRequired[
        "capo_bedrock_agentcore_control.types.ephemeral_ebs_volume_configuration.EphemeralEBSVolumeConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralBlockDeviceMapping) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "virtual_name" in value:
        out["virtualName"] = value["virtual_name"]
    if "ebs" in value:
        import capo_bedrock_agentcore_control.types.ephemeral_ebs_volume_configuration

        out["ebs"] = (
            capo_bedrock_agentcore_control.types.ephemeral_ebs_volume_configuration.serialize_json(
                value["ebs"]
            )
        )
    return out


def deserialize_json(data: dict) -> EphemeralBlockDeviceMapping:
    out: EphemeralBlockDeviceMapping = {}  # type: ignore[typeddict-item]
    if data.get("deviceName") is not None:
        out["device_name"] = data["deviceName"]
    if data.get("virtualName") is not None:
        out["virtual_name"] = data["virtualName"]
    if data.get("ebs") is not None:
        import capo_bedrock_agentcore_control.types.ephemeral_ebs_volume_configuration

        out["ebs"] = (
            capo_bedrock_agentcore_control.types.ephemeral_ebs_volume_configuration.deserialize_json(
                data["ebs"]
            )
        )
    return out
