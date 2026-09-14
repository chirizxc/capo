"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPluginRevisionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__long
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601
    import capo_kafkaconnect.types.custom_plugin_content_type
    import capo_kafkaconnect.types.custom_plugin_file_description
    import capo_kafkaconnect.types.custom_plugin_location_description


class CustomPluginRevisionSummary(TypedDict, closed=True):
    content_type: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_content_type.CustomPluginContentType"
    ]
    """<p>The format of the plugin file.</p>"""
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the custom plugin was created.</p>"""
    description: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The description of the custom plugin.</p>"""
    file_description: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_file_description.CustomPluginFileDescription"
    ]
    """<p>Details about the custom plugin file.</p>"""
    location: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_location_description.CustomPluginLocationDescription"
    ]
    """<p>Information about the location of the custom plugin.</p>"""
    revision: "capo_kafkaconnect.types.__long.__long"
    """<p>The revision of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginRevisionSummary) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "file_description" in value:
        import capo_kafkaconnect.types.custom_plugin_file_description

        out["fileDescription"] = (
            capo_kafkaconnect.types.custom_plugin_file_description.serialize_json(
                value["file_description"]
            )
        )
    if "location" in value:
        import capo_kafkaconnect.types.custom_plugin_location_description

        out["location"] = (
            capo_kafkaconnect.types.custom_plugin_location_description.serialize_json(
                value["location"]
            )
        )
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> CustomPluginRevisionSummary:
    out: CustomPluginRevisionSummary = {}  # type: ignore[typeddict-item]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("creationTime") is not None:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("fileDescription") is not None:
        import capo_kafkaconnect.types.custom_plugin_file_description

        out["file_description"] = (
            capo_kafkaconnect.types.custom_plugin_file_description.deserialize_json(
                data["fileDescription"]
            )
        )
    if data.get("location") is not None:
        import capo_kafkaconnect.types.custom_plugin_location_description

        out["location"] = (
            capo_kafkaconnect.types.custom_plugin_location_description.deserialize_json(
                data["location"]
            )
        )
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
