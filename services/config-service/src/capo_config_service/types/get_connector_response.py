"""Generated from Smithy shape ``com.amazonaws.configservice#GetConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.connector


class GetConnectorResponse(TypedDict, closed=True):
    connector: "capo_config_service.types.connector.Connector"
    """<p>The details of the specified connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectorResponse) -> dict:
    out: dict = {}
    import capo_config_service.types.connector

    out["Connector"] = capo_config_service.types.connector.serialize_aws_json_1_1(
        value["connector"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectorResponse:
    out: GetConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("Connector") is not None:
        import capo_config_service.types.connector

        out["connector"] = capo_config_service.types.connector.deserialize_aws_json_1_1(
            data["Connector"]
        )
    else:
        raise DeserializationError("GetConnectorResponse.connector required")
    return out
