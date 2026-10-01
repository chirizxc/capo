"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RotatePaymentConnectorCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_status
    import capo_bedrock_agentcore_control.types.payment_manager_id


class RotatePaymentConnectorCredentialsResponse(TypedDict, closed=True):
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector.</p>"""
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the parent payment manager.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was last updated, which is when the rotation completed.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector, which is <code>READY</code> after a successful rotation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RotatePaymentConnectorCredentialsResponse) -> dict:
    out: dict = {}
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentManagerId"] = value["payment_manager_id"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> RotatePaymentConnectorCredentialsResponse:
    out: RotatePaymentConnectorCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "RotatePaymentConnectorCredentialsResponse.payment_connector_id required"
        )
    if data.get("paymentManagerId") is not None:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError(
            "RotatePaymentConnectorCredentialsResponse.payment_manager_id required"
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "RotatePaymentConnectorCredentialsResponse.last_updated_at required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "RotatePaymentConnectorCredentialsResponse.status required"
        )
    return out
