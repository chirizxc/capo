"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSPosixFileSystemUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_system_gid
    import capo_fsx.types.file_system_secondary_gi_ds
    import capo_fsx.types.file_system_uid


class OpenZFSPosixFileSystemUser(TypedDict, closed=True):
    uid: NotRequired["capo_fsx.types.file_system_uid.FileSystemUID"]
    """<p>The UID of the file system user.</p>"""
    gid: NotRequired["capo_fsx.types.file_system_gid.FileSystemGID"]
    """<p>The GID of the file system user.</p>"""
    secondary_gids: NotRequired[
        "capo_fsx.types.file_system_secondary_gi_ds.FileSystemSecondaryGIDs"
    ]
    """<p>The list of secondary GIDs for the file system user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSPosixFileSystemUser) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "gid" in value:
        out["Gid"] = value["gid"]
    if "secondary_gids" in value:
        import capo_fsx.types.file_system_secondary_gi_ds

        out["SecondaryGids"] = (
            capo_fsx.types.file_system_secondary_gi_ds.serialize_aws_json_1_1(
                value["secondary_gids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSPosixFileSystemUser:
    out: OpenZFSPosixFileSystemUser = {}  # type: ignore[typeddict-item]
    if data.get("Uid") is not None:
        out["uid"] = data["Uid"]
    if data.get("Gid") is not None:
        out["gid"] = data["Gid"]
    if data.get("SecondaryGids") is not None:
        import capo_fsx.types.file_system_secondary_gi_ds

        out["secondary_gids"] = (
            capo_fsx.types.file_system_secondary_gi_ds.deserialize_aws_json_1_1(
                data["SecondaryGids"]
            )
        )
    return out
