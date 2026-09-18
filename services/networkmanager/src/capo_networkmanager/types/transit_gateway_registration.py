"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRegistration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.transit_gateway_arn
    import capo_networkmanager.types.transit_gateway_registration_state_reason


class TransitGatewayRegistration(TypedDict, closed=True):
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    transit_gateway_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""
    state: NotRequired[
        "capo_networkmanager.types.transit_gateway_registration_state_reason.TransitGatewayRegistrationStateReason"
    ]
    """<p>The state of the transit gateway registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayRegistration) -> dict:
    out: dict = {}
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "transit_gateway_arn" in value:
        out["TransitGatewayArn"] = value["transit_gateway_arn"]
    if "state" in value:
        import capo_networkmanager.types.transit_gateway_registration_state_reason

        out["State"] = (
            capo_networkmanager.types.transit_gateway_registration_state_reason.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransitGatewayRegistration:
    out: TransitGatewayRegistration = {}  # type: ignore[typeddict-item]
    if data.get("GlobalNetworkId") is not None:
        out["global_network_id"] = data["GlobalNetworkId"]
    if data.get("TransitGatewayArn") is not None:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    if data.get("State") is not None:
        import capo_networkmanager.types.transit_gateway_registration_state_reason

        out["state"] = (
            capo_networkmanager.types.transit_gateway_registration_state_reason.deserialize_json(
                data["State"]
            )
        )
    return out
