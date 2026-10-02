"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateConnectorV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.connector_status
    import capo_securityhub.types.enablement_status


class UpdateConnectorV2Response(TypedDict, closed=True):
    connector_status: NotRequired[
        "capo_securityhub.types.connector_status.ConnectorStatus"
    ]
    """<p>The status of the connector after the update.</p>"""
    enablement_status: NotRequired[
        "capo_securityhub.types.enablement_status.EnablementStatus"
    ]
    """<p>The enablement status of the connector after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorV2Response) -> dict:
    out: dict = {}
    if "connector_status" in value:
        import capo_securityhub.types.connector_status

        out["ConnectorStatus"] = capo_securityhub.types.connector_status.serialize_json(
            value["connector_status"]
        )
    if "enablement_status" in value:
        import capo_securityhub.types.enablement_status

        out["EnablementStatus"] = (
            capo_securityhub.types.enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorV2Response:
    out: UpdateConnectorV2Response = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorStatus") is not None:
        import capo_securityhub.types.connector_status

        out["connector_status"] = (
            capo_securityhub.types.connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    if data.get("EnablementStatus") is not None:
        import capo_securityhub.types.enablement_status

        out["enablement_status"] = (
            capo_securityhub.types.enablement_status.deserialize_json(
                data["EnablementStatus"]
            )
        )
    return out
