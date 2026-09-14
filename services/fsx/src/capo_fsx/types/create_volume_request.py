"""Generated from Smithy shape ``com.amazonaws.fsx#CreateVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.create_ontap_volume_configuration
    import capo_fsx.types.create_open_zfs_volume_configuration
    import capo_fsx.types.tags
    import capo_fsx.types.volume_name
    import capo_fsx.types.volume_type


class CreateVolumeRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    volume_type: NotRequired["capo_fsx.types.volume_type.VolumeType"]
    """<p>Specifies the type of volume to create; <code>ONTAP</code> and <code>OPENZFS</code> are the only valid volume types.</p>"""
    name: NotRequired["capo_fsx.types.volume_name.VolumeName"]
    """<p>Specifies the name of the volume that you're creating.</p>"""
    ontap_configuration: NotRequired[
        "capo_fsx.types.create_ontap_volume_configuration.CreateOntapVolumeConfiguration"
    ]
    """<p>Specifies the configuration to use when creating the ONTAP volume.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    open_zfs_configuration: NotRequired[
        "capo_fsx.types.create_open_zfs_volume_configuration.CreateOpenZFSVolumeConfiguration"
    ]
    """<p>Specifies the configuration to use when creating the OpenZFS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVolumeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_type" in value:
        import capo_fsx.types.volume_type

        out["VolumeType"] = capo_fsx.types.volume_type.serialize_aws_json_1_1(
            value["volume_type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "ontap_configuration" in value:
        import capo_fsx.types.create_ontap_volume_configuration

        out["OntapConfiguration"] = (
            capo_fsx.types.create_ontap_volume_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "open_zfs_configuration" in value:
        import capo_fsx.types.create_open_zfs_volume_configuration

        out["OpenZFSConfiguration"] = (
            capo_fsx.types.create_open_zfs_volume_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVolumeRequest:
    out: CreateVolumeRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("VolumeType") is not None:
        import capo_fsx.types.volume_type

        out["volume_type"] = capo_fsx.types.volume_type.deserialize_aws_json_1_1(
            data["VolumeType"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OntapConfiguration") is not None:
        import capo_fsx.types.create_ontap_volume_configuration

        out["ontap_configuration"] = (
            capo_fsx.types.create_ontap_volume_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("OpenZFSConfiguration") is not None:
        import capo_fsx.types.create_open_zfs_volume_configuration

        out["open_zfs_configuration"] = (
            capo_fsx.types.create_open_zfs_volume_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out
