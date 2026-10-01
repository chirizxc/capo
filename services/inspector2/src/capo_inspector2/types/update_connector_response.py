"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn


class UpdateConnectorResponse(TypedDict, closed=True):
    connector_arn: NotRequired["capo_inspector2.types.connector_arn.ConnectorArn"]
    """<p>The Amazon Resource Name (ARN) of the updated connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConnectorResponse:
    out: UpdateConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    return out
