"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateCloudConnectorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_id


class UpdateCloudConnectorResult(TypedDict, closed=True):
    cloud_connector_id: NotRequired[
        "capo_ssm.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The ID of the cloud connector that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCloudConnectorResult) -> dict:
    out: dict = {}
    if "cloud_connector_id" in value:
        out["CloudConnectorId"] = value["cloud_connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCloudConnectorResult:
    out: UpdateCloudConnectorResult = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    return out
