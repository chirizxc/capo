"""Generated from Smithy shape ``com.amazonaws.eks#KubeSchedulerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.node_resources_fit_config


class KubeSchedulerConfigResponse(TypedDict, closed=True):
    node_resources_fit: NotRequired[
        "capo_eks.types.node_resources_fit_config.NodeResourcesFitConfig"
    ]
    """<p>The node resource fit scoring configuration for the scheduler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeSchedulerConfigResponse) -> dict:
    out: dict = {}
    if "node_resources_fit" in value:
        import capo_eks.types.node_resources_fit_config

        out["nodeResourcesFit"] = (
            capo_eks.types.node_resources_fit_config.serialize_json(
                value["node_resources_fit"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeSchedulerConfigResponse:
    out: KubeSchedulerConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("nodeResourcesFit") is not None:
        import capo_eks.types.node_resources_fit_config

        out["node_resources_fit"] = (
            capo_eks.types.node_resources_fit_config.deserialize_json(
                data["nodeResourcesFit"]
            )
        )
    return out
