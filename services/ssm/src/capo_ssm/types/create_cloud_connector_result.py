"""Generated from Smithy shape ``com.amazonaws.ssm#CreateCloudConnectorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_id


class CreateCloudConnectorResult(TypedDict, closed=True):
    cloud_connector_id: NotRequired[
        "capo_ssm.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The ID of the cloud connector that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCloudConnectorResult) -> dict:
    out: dict = {}
    if "cloud_connector_id" in value:
        out["CloudConnectorId"] = value["cloud_connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCloudConnectorResult:
    out: CreateCloudConnectorResult = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    return out
