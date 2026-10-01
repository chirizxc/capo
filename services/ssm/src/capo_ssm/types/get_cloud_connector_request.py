"""Generated from Smithy shape ``com.amazonaws.ssm#GetCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_id


class GetCloudConnectorRequest(TypedDict, closed=True):
    cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId"
    """<p>The ID of the cloud connector to retrieve information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCloudConnectorRequest) -> dict:
    out: dict = {}
    out["CloudConnectorId"] = value["cloud_connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCloudConnectorRequest:
    out: GetCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    else:
        raise DeserializationError(
            "GetCloudConnectorRequest.cloud_connector_id required"
        )
    return out
