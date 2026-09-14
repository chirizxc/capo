"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateLoggerDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class CreateLoggerDefinitionResponse(TypedDict, closed=True):
    arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the definition."""
    creation_timestamp: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the definition was created."""
    id: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the definition."""
    last_updated_timestamp: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the definition was last updated."""
    latest_version: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the latest version associated with the definition."""
    latest_version_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the latest version associated with the definition."""
    name: NotRequired["capo_greengrass.types.__string.__string"]
    """The name of the definition."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggerDefinitionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    if "id" in value:
        out["Id"] = value["id"]
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "latest_version" in value:
        out["LatestVersion"] = value["latest_version"]
    if "latest_version_arn" in value:
        out["LatestVersionArn"] = value["latest_version_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateLoggerDefinitionResponse:
    out: CreateLoggerDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationTimestamp") is not None:
        out["creation_timestamp"] = data["CreationTimestamp"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("LastUpdatedTimestamp") is not None:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if data.get("LatestVersion") is not None:
        out["latest_version"] = data["LatestVersion"]
    if data.get("LatestVersionArn") is not None:
        out["latest_version_arn"] = data["LatestVersionArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
