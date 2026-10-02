"""Generated from Smithy shape ``com.amazonaws.configservice#Connector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.connector_configuration
    import capo_config_service.types.connector_name
    import capo_config_service.types.date


class Connector(TypedDict, closed=True):
    name: "capo_config_service.types.connector_name.ConnectorName"
    """<p>The name of the connector.</p>"""
    arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_configuration: (
        "capo_config_service.types.connector_configuration.ConnectorConfiguration"
    )
    """<p>The provider-specific configuration for connecting to the third-party cloud service provider.</p>"""
    created_time: "capo_config_service.types.date.Date"
    """<p>The date and time that the connector was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connector) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_config_service.types.connector_configuration

    out["connectorConfiguration"] = (
        capo_config_service.types.connector_configuration.serialize_aws_json_1_1(
            value["connector_configuration"]
        )
    )
    import capo_config_service.types.date

    out["createdTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
        value["created_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Connector.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Connector.arn required")
    if data.get("connectorConfiguration") is not None:
        import capo_config_service.types.connector_configuration

        out["connector_configuration"] = (
            capo_config_service.types.connector_configuration.deserialize_aws_json_1_1(
                data["connectorConfiguration"]
            )
        )
    else:
        raise DeserializationError("Connector.connector_configuration required")
    if data.get("createdTime") is not None:
        import capo_config_service.types.date

        out["created_time"] = capo_config_service.types.date.deserialize_aws_json_1_1(
            data["createdTime"]
        )
    else:
        raise DeserializationError("Connector.created_time required")
    return out
