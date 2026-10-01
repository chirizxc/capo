"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EphemeralEBSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ebs_card_index
    import capo_bedrock_agentcore_control.types.ebs_snapshot_id
    import capo_bedrock_agentcore_control.types.ebs_volume_initialization_rate
    import capo_bedrock_agentcore_control.types.ebs_volume_type
    import capo_bedrock_agentcore_control.types.kms_key_id
    import capo_bedrock_agentcore_control.types.volume_iops
    import capo_bedrock_agentcore_control.types.volume_size_gi_b
    import capo_bedrock_agentcore_control.types.volume_throughput


class EphemeralEBSVolumeConfiguration(TypedDict, closed=True):
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
    snapshot_id: NotRequired[
        "capo_bedrock_agentcore_control.types.ebs_snapshot_id.EbsSnapshotId"
    ]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired[
        "capo_bedrock_agentcore_control.types.volume_size_gi_b.VolumeSizeGiB"
    ]
    """<p>The size of the volume, in GiB. You must specify either a snapshot ID or a volume size. Supported sizes: <code>gp2</code>, 1–16,384; <code>gp3</code>, 1–65,536; <code>io1</code>, 4–16,384; <code>io2</code>, 4–65,536.</p>"""
    volume_initialization_rate: NotRequired[
        "capo_bedrock_agentcore_control.types.ebs_volume_initialization_rate.EbsVolumeInitializationRate"
    ]
    """<p>The rate at which the volume is initialized after creation, in MiB/s. Supported only for volumes created from snapshots. Valid range: 100–300 MiB/s.</p>"""
    ebs_card_index: NotRequired[
        "capo_bedrock_agentcore_control.types.ebs_card_index.EbsCardIndex"
    ]
    """<p>The index of the Amazon EBS card. Applies to instances with multiple Amazon EBS cards.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralEBSVolumeConfiguration) -> dict:
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
    if "snapshot_id" in value:
        out["snapshotId"] = value["snapshot_id"]
    if "volume_size" in value:
        out["volumeSize"] = value["volume_size"]
    if "volume_initialization_rate" in value:
        out["volumeInitializationRate"] = value["volume_initialization_rate"]
    if "ebs_card_index" in value:
        out["ebsCardIndex"] = value["ebs_card_index"]
    return out


def deserialize_json(data: dict) -> EphemeralEBSVolumeConfiguration:
    out: EphemeralEBSVolumeConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("snapshotId") is not None:
        out["snapshot_id"] = data["snapshotId"]
    if data.get("volumeSize") is not None:
        out["volume_size"] = data["volumeSize"]
    if data.get("volumeInitializationRate") is not None:
        out["volume_initialization_rate"] = data["volumeInitializationRate"]
    if data.get("ebsCardIndex") is not None:
        out["ebs_card_index"] = data["ebsCardIndex"]
    return out
