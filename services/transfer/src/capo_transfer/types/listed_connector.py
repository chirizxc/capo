"""Generated from Smithy shape ``com.amazonaws.transfer#ListedConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.connector_id
    import capo_transfer.types.url


class ListedConnector(TypedDict, closed=True):
    arn: NotRequired["capo_transfer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the specified connector.</p>"""
    connector_id: NotRequired["capo_transfer.types.connector_id.ConnectorId"]
    """<p>The unique identifier for the connector.</p>"""
    url: NotRequired["capo_transfer.types.url.Url"]
    """<p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedConnector) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedConnector:
    out: ListedConnector = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
