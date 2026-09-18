"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateGroupVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class CreateGroupVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    connector_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the connector definition version for this group."""
    core_definition_version_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the core definition version for this group."""
    device_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the device definition version for this group."""
    function_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the function definition version for this group."""
    group_id: "capo_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""
    logger_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the logger definition version for this group."""
    resource_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the resource definition version for this group."""
    subscription_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the subscription definition version for this group."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupVersionRequest) -> dict:
    out: dict = {}
    if "connector_definition_version_arn" in value:
        out["ConnectorDefinitionVersionArn"] = value["connector_definition_version_arn"]
    if "core_definition_version_arn" in value:
        out["CoreDefinitionVersionArn"] = value["core_definition_version_arn"]
    if "device_definition_version_arn" in value:
        out["DeviceDefinitionVersionArn"] = value["device_definition_version_arn"]
    if "function_definition_version_arn" in value:
        out["FunctionDefinitionVersionArn"] = value["function_definition_version_arn"]
    if "logger_definition_version_arn" in value:
        out["LoggerDefinitionVersionArn"] = value["logger_definition_version_arn"]
    if "resource_definition_version_arn" in value:
        out["ResourceDefinitionVersionArn"] = value["resource_definition_version_arn"]
    if "subscription_definition_version_arn" in value:
        out["SubscriptionDefinitionVersionArn"] = value[
            "subscription_definition_version_arn"
        ]
    return out


def deserialize_json(data: dict) -> CreateGroupVersionRequest:
    out: CreateGroupVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorDefinitionVersionArn") is not None:
        out["connector_definition_version_arn"] = data["ConnectorDefinitionVersionArn"]
    if data.get("CoreDefinitionVersionArn") is not None:
        out["core_definition_version_arn"] = data["CoreDefinitionVersionArn"]
    if data.get("DeviceDefinitionVersionArn") is not None:
        out["device_definition_version_arn"] = data["DeviceDefinitionVersionArn"]
    if data.get("FunctionDefinitionVersionArn") is not None:
        out["function_definition_version_arn"] = data["FunctionDefinitionVersionArn"]
    if data.get("LoggerDefinitionVersionArn") is not None:
        out["logger_definition_version_arn"] = data["LoggerDefinitionVersionArn"]
    if data.get("ResourceDefinitionVersionArn") is not None:
        out["resource_definition_version_arn"] = data["ResourceDefinitionVersionArn"]
    if data.get("SubscriptionDefinitionVersionArn") is not None:
        out["subscription_definition_version_arn"] = data[
            "SubscriptionDefinitionVersionArn"
        ]
    return out
