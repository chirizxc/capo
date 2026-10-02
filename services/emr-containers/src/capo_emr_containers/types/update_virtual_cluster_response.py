"""Generated from Smithy shape ``com.amazonaws.emrcontainers#UpdateVirtualClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.virtual_cluster


class UpdateVirtualClusterResponse(TypedDict, closed=True):
    virtual_cluster: NotRequired[
        "capo_emr_containers.types.virtual_cluster.VirtualCluster"
    ]
    """<p>The updated virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualClusterResponse) -> dict:
    out: dict = {}
    if "virtual_cluster" in value:
        import capo_emr_containers.types.virtual_cluster

        out["virtualCluster"] = (
            capo_emr_containers.types.virtual_cluster.serialize_json(
                value["virtual_cluster"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVirtualClusterResponse:
    out: UpdateVirtualClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualCluster") is not None:
        import capo_emr_containers.types.virtual_cluster

        out["virtual_cluster"] = (
            capo_emr_containers.types.virtual_cluster.deserialize_json(
                data["virtualCluster"]
            )
        )
    return out
