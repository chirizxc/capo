"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorDestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cloud_connector_id
    import capo_iot_managed_integrations.types.connector_destination_description
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.connector_destination_name


class ConnectorDestinationSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
    ]
    """<p>The display name of the connector destination.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
    ]
    """<p>A description of the connector destination.</p>"""
    cloud_connector_id: NotRequired[
        "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The identifier of the cloud connector associated with this connector destination.</p>"""
    id: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The unique identifier of the connector destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorDestinationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "cloud_connector_id" in value:
        out["CloudConnectorId"] = value["cloud_connector_id"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ConnectorDestinationSummary:
    out: ConnectorDestinationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
