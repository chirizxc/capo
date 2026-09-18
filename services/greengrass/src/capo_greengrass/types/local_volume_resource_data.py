"""Generated from Smithy shape ``com.amazonaws.greengrass#LocalVolumeResourceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.group_owner_setting


class LocalVolumeResourceData(TypedDict, closed=True):
    destination_path: NotRequired["capo_greengrass.types.__string.__string"]
    """The absolute local path of the resource inside the Lambda environment."""
    group_owner_setting: NotRequired[
        "capo_greengrass.types.group_owner_setting.GroupOwnerSetting"
    ]
    """Allows you to configure additional group privileges for the Lambda process. This field is optional."""
    source_path: NotRequired["capo_greengrass.types.__string.__string"]
    """The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with ''/sys''."""


# --- restJson1 ser/de ---
def serialize_json(value: LocalVolumeResourceData) -> dict:
    out: dict = {}
    if "destination_path" in value:
        out["DestinationPath"] = value["destination_path"]
    if "group_owner_setting" in value:
        import capo_greengrass.types.group_owner_setting

        out["GroupOwnerSetting"] = (
            capo_greengrass.types.group_owner_setting.serialize_json(
                value["group_owner_setting"]
            )
        )
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    return out


def deserialize_json(data: dict) -> LocalVolumeResourceData:
    out: LocalVolumeResourceData = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPath") is not None:
        out["destination_path"] = data["DestinationPath"]
    if data.get("GroupOwnerSetting") is not None:
        import capo_greengrass.types.group_owner_setting

        out["group_owner_setting"] = (
            capo_greengrass.types.group_owner_setting.deserialize_json(
                data["GroupOwnerSetting"]
            )
        )
    if data.get("SourcePath") is not None:
        out["source_path"] = data["SourcePath"]
    return out
