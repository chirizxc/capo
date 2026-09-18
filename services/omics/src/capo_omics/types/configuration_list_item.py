"""Generated from Smithy shape ``com.amazonaws.omics#ConfigurationListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.configuration_arn
    import capo_omics.types.configuration_description
    import capo_omics.types.configuration_name
    import capo_omics.types.configuration_status
    import capo_omics.types.configuration_timestamp


class ConfigurationListItem(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.configuration_arn.ConfigurationArn"]
    """<p>Unique resource identifier for the configuration.</p>"""
    name: NotRequired["capo_omics.types.configuration_name.ConfigurationName"]
    """<p>User-friendly name for the configuration.</p>"""
    description: NotRequired[
        "capo_omics.types.configuration_description.ConfigurationDescription"
    ]
    """<p>Description for the configuration.</p>"""
    status: NotRequired["capo_omics.types.configuration_status.ConfigurationStatus"]
    """<p>Current configuration status.</p>"""
    creation_time: NotRequired[
        "capo_omics.types.configuration_timestamp.ConfigurationTimestamp"
    ]
    """<p>Configuration creation timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import capo_omics.types.configuration_timestamp

        out["creationTime"] = capo_omics.types.configuration_timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> ConfigurationListItem:
    out: ConfigurationListItem = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("creationTime") is not None:
        import capo_omics.types.configuration_timestamp

        out["creation_time"] = (
            capo_omics.types.configuration_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    return out
