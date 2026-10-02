"""Generated from Smithy shape ``com.amazonaws.configservice#PutConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.connector_configuration
    import capo_config_service.types.tags_list


class PutConnectorRequest(TypedDict, closed=True):
    connector_configuration: (
        "capo_config_service.types.connector_configuration.ConnectorConfiguration"
    )
    """<p>The provider-specific configuration for connecting to the third-party cloud service provider.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for the connector. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConnectorRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.connector_configuration

    out["ConnectorConfiguration"] = (
        capo_config_service.types.connector_configuration.serialize_aws_json_1_1(
            value["connector_configuration"]
        )
    )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConnectorRequest:
    out: PutConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorConfiguration") is not None:
        import capo_config_service.types.connector_configuration

        out["connector_configuration"] = (
            capo_config_service.types.connector_configuration.deserialize_aws_json_1_1(
                data["ConnectorConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutConnectorRequest.connector_configuration required"
        )
    if data.get("Tags") is not None:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
