"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkResourceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_resource_association_arn
    import capo_vpc_lattice.types.service_network_resource_association_id
    import capo_vpc_lattice.types.service_network_resource_association_status


class DeleteServiceNetworkResourceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_resource_association_id.ServiceNetworkResourceAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_resource_association_arn.ServiceNetworkResourceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_resource_association_status.ServiceNetworkResourceAssociationStatus"
    ]
    """<p>The status of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkResourceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkResourceAssociationResponse:
    out: DeleteServiceNetworkResourceAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
