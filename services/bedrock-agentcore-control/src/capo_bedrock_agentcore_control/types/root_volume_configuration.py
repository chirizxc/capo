"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RootVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ebs_volume_type
    import capo_bedrock_agentcore_control.types.kms_key_id
    import capo_bedrock_agentcore_control.types.volume_iops
    import capo_bedrock_agentcore_control.types.volume_size_gi_b
    import capo_bedrock_agentcore_control.types.volume_throughput


class RootVolumeConfiguration(TypedDict, closed=True):
    volume_type: "capo_bedrock_agentcore_control.types.ebs_volume_type.EbsVolumeType"
    """<p>The Amazon EBS volume type. If you do not specify a type, the default is <code>gp3</code>.</p>"""
    iops: NotRequired["capo_bedrock_agentcore_control.types.volume_iops.VolumeIops"]
    """<p>The number of IOPS to provision. For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this is the number of IOPS provisioned for the volume. For <code>gp2</code> volumes, this sets the baseline IOPS performance. It also controls the rate at which the volume accumulates I/O credits for bursting. Supported values: <code>gp3</code>, 3,000–80,000; <code>io1</code>, 100–64,000; <code>io2</code>, 100–256,000.</p>"""
    throughput: NotRequired[
        "capo_bedrock_agentcore_control.types.volume_throughput.VolumeThroughput"
    ]
    """<p>The throughput to provision, in MiB/s. Valid only for <code>gp3</code> volumes. Valid range: 125–2,000 MiB/s.</p>"""
    encrypted: NotRequired["bool"]
    """<p>Specifies whether to encrypt the volume. Encrypted volumes can be attached only to instances that support Amazon EBS encryption. If you create a volume from a snapshot, you cannot specify an encryption value.</p>"""
    kms_key_id: NotRequired["capo_bedrock_agentcore_control.types.kms_key_id.KmsKeyId"]
    """<p>The identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for Amazon EBS encryption.</p>"""
    free_space_gi_b: NotRequired[
        "capo_bedrock_agentcore_control.types.volume_size_gi_b.VolumeSizeGiB"
    ]
    """<p>The free space guaranteed on the root volume, in GiB. AgentCore adds the operating system overhead on top of this value. The default is 8 GiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RootVolumeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.ebs_volume_type

    out["volumeType"] = (
        capo_bedrock_agentcore_control.types.ebs_volume_type.serialize_json(
            value.get("volume_type", "gp3")
        )
    )
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "free_space_gi_b" in value:
        out["freeSpaceGiB"] = value["free_space_gi_b"]
    return out


def deserialize_json(data: dict) -> RootVolumeConfiguration:
    out: RootVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("volumeType") is not None:
        import capo_bedrock_agentcore_control.types.ebs_volume_type

        out["volume_type"] = (
            capo_bedrock_agentcore_control.types.ebs_volume_type.deserialize_json(
                data["volumeType"]
            )
        )
    else:
        out["volume_type"] = "gp3"
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    if data.get("encrypted") is not None:
        out["encrypted"] = data["encrypted"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("freeSpaceGiB") is not None:
        out["free_space_gi_b"] = data["freeSpaceGiB"]
    return out
