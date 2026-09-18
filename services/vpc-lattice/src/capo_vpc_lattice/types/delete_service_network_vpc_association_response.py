"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkVpcAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_vpc_association_arn
    import capo_vpc_lattice.types.service_network_vpc_association_id
    import capo_vpc_lattice.types.service_network_vpc_association_status


class DeleteServiceNetworkVpcAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_id.ServiceNetworkVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_status.ServiceNetworkVpcAssociationStatus"
    ]
    """<p>The status. You can retry the operation if the status is <code>DELETE_FAILED</code>. However, if you retry it while the status is <code>DELETE_IN_PROGRESS</code>, there is no change in the status.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_arn.ServiceNetworkVpcAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkVpcAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkVpcAssociationResponse:
    out: DeleteServiceNetworkVpcAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
