"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourceGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.resource_gateway_arn
    import capo_vpc_lattice.types.resource_gateway_id
    import capo_vpc_lattice.types.resource_gateway_name
    import capo_vpc_lattice.types.resource_gateway_status


class DeleteResourceGatewayResponse(TypedDict, closed=True):
    id: NotRequired["capo_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"]
    """<p>The ID of the resource gateway.</p>"""
    arn: NotRequired["capo_vpc_lattice.types.resource_gateway_arn.ResourceGatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the resource gateway.</p>"""
    name: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_name.ResourceGatewayName"
    ]
    """<p>The name of the resource gateway.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_status.ResourceGatewayStatus"
    ]
    """<p>The status of the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceGatewayResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteResourceGatewayResponse:
    out: DeleteResourceGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
